import time
import webbrowser

def open_tabs():
    # URLs of the tabs you want to open
    urls = [
        'https://www.youtube.com/watch?v=3B8qYBBml68&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=102&t=20s',
        'https://www.youtube.com',
        'https://drive.google.com/drive/folders/156T5RqUng7VLCjX_0d9sR7GpY2BQUE4H',
        'https://www.hackerrank.com',
        'https://myu.mans.edu.eg/',
        'https://leetcode.com/problemset/all/?sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d',
        'https://chat.openai.com/?model=text-davinci-002-render-sha',
        "https://codeforces.com/problemset/"
    ]

    # Open each URL in a new tab
    for url in urls:
        webbrowser.open_new_tab(url)

def main():
    # Delay in seconds before opening the tabs (2 minutes = 120 seconds)
    delay_seconds = 2

    print(f"Waiting for {delay_seconds} seconds...")
    time.sleep(delay_seconds)

    print("Opening tabs...")
    open_tabs()

if __name__ == "__main__":
    main()

                


