import sys
import requests
from bs4 import BeautifulSoup
import markdown

def parse_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 针对微信公众号的特殊处理
        if "mp.weixin.qq.com" in url:
            content_div = soup.find('div', id='js_content')
            title = soup.find('h1', id='activity-name').get_text(strip=True)
        else:
            # 通用处理：尝试寻找 article 标签或 body
            content_div = soup.find('article') or soup.find('main') or soup.body
            title = soup.title.string if soup.title else "Untitled"

        if content_div:
            # 简单清理：移除脚本和样式
            for script in content_div(["script", "style"]):
                script.decompose()
            text = content_div.get_text(separator='\n', strip=True)
            return f"# {title}\n\n{text}"
        else:
            return "未能识别正文内容。"
            
    except Exception as e:
        return f"错误: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 parser.py <URL>")
    else:
        print(parse_url(sys.argv[1]))
