# PREMIUM
class Video:
    def __init__(self, videoId, content):
        self.videoId = videoId
        self.content = content
        self.like = 0
        self.dislike = 0
        self.views = 0

class IdManager:
    def __init__(self):
        self.heap = []
        self.next_id = -1

    def get_id(self):
        if self.heap:
            return heappop(self.heap)
        else:
            self.next_id += 1
            return self.next_id

    def add_id(self, videoId):
        heappush(self.heap, videoId)


class VideoSharingPlatform:
    def __init__(self):
        self.db = {}
        self.idm = IdManager()
        
    def upload(self, video: str) -> int:
        curr_id = self.idm.get_id()
        video = Video(curr_id, video)
        self.db[curr_id] = video
        return curr_id

    def remove(self, videoId: int) -> None:
        if videoId not in self.db:
            return

        video = self.db[videoId]
        self.idm.add_id(video.videoId)
        del self.db[video.videoId]
        

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.db:
            return '-1'

        video = self.db[videoId]
        video.views += 1
        return video.content[startMinute:endMinute+1]

    def like(self, videoId: int) -> None:
        if videoId not in self.db:
            return

        video = self.db[videoId]
        video.like += 1

    def dislike(self, videoId: int) -> None:
        if videoId not in self.db:
            return

        video = self.db[videoId]
        video.dislike += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.db:
            return [-1]

        video = self.db[videoId]
        return [video.like, video.dislike]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.db:
            return -1

        video = self.db[videoId]
        return video.views


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)