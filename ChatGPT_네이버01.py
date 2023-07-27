import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook

def crawl_blog_info(search_keyword, num_pages=100):
    wb = Workbook()
    ws = wb.active
    ws.append(["Blog URL", "Title", "Post Date"])

    for page in range(1, num_pages + 1):
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page*10-9}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            blog_entries = soup.find_all("li", class_="bx")

            if not blog_entries:
                print("No more results.")
                break

            print(f"==== Page {page} ====")

            for entry in blog_entries:
                try:
                    blog_url = entry.find("a", class_="api_txt_lines").get("href")
                    blog_title = entry.find("a", class_="api_txt_lines").text
                    post_date = entry.find("span", class_="sub_time").text

                    ws.append([blog_url, blog_title, post_date])
                    print(f"Blog URL: {blog_url}")
                    print(f"Title: {blog_title}")
                    print(f"Post Date: {post_date}\n")
                except AttributeError:
                    # If any of the required elements are not found, skip to the next entry.
                    continue
        else:
            print(f"Failed to fetch the data. Status Code: {response.status_code}")

    wb.save(r"c:\work\blog_results.xlsx")

if __name__ == "__main__":
    # search_keyword = input("Enter the search keyword: ")
    search_keyword = "맥북에어"
    crawl_blog_info(search_keyword)
