# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from urllib.parse import urlparse
class Solution:
    def _getHostName(self, url):
        parsed_url = urlparse(url)
        return parsed_url.hostname

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        startHost = self._getHostName(startUrl)
        parsedUrl = []
        
        visited = set([startUrl])
        que = deque([startUrl])
        

        while que:
            currUrl = que.popleft()
            currHost = self._getHostName(currUrl)

            if currHost == startHost:
                parsedUrl.append(currUrl)
            else:
                continue

            for linkedURL in htmlParser.getUrls(currUrl):
                if linkedURL in visited:
                    continue
                visited.add(linkedURL)
                que.append(linkedURL)

        return parsedUrl