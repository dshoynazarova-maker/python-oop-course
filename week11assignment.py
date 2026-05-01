from dataclasses import dataclass, field

class TrackError(Exception):
    pass

@dataclass
class Track:
    code: str
    title: str
    genre: str
    duration: int
    _status: str = field(default="PENDING", init=False)

    def __post_init__(self):
        if self.duration <= 0:
            raise TrackError(f'!!! Error: Invalid duration for {self.code}')
        
    @property
    def minutes(self):
        return round((self.duration/60),1)
    
    def __str__(self):
        return f'[{self.code}] {self.title} ({self.genre}, {self.duration}s) -> {self._status}'
    
    def __gt__(self,other):
        return self.duration > other.duration
    
class PlaylistFilter:
    def __init__(self, tracks, genres):
        self._tracks = tracks
        self.genres = set(genres)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        #music = self.tracks[self.index]
        if self._index >= len(self._tracks):
            raise StopIteration

        music = self._tracks[self._index]
        self._index += 1

        if music.genre in self.genres:
            music._status = 'QUEUED'
        else:
            music._status = 'SKIPPED'
        
        return music
    
def playlist_report(filt: PlaylistFilter ):
    counts_queued = 0
    skipped_tracks = 0

    for music in filt:
        if music._status == 'QUEUED':
            counts_queued += 1
        else:
            skipped_tracks +=1
        yield str(music)
    yield f"Summary: {counts_queued} queued, {skipped_tracks} skipped"


class PlaylistSession:
    def __init__(self, name):
        self.name = name
        self._tracks = []

    def __enter__(self):
        print(f"=== Playing: {self.name} ===")
        return self
    
    def add(self, track):
        self._tracks.append(track)

    def filter(self, genres):
        filterator = PlaylistFilter(self._tracks, genres)
        return playlist_report(filterator)
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type is TrackError:
            print(f'{exc}')
            print(f"=== Stopped: {self.name} ({len(self._tracks)} tracks) ===")
            return True

        print(f"=== Stopped: {self.name} ({len(self._tracks)} tracks) ===")
        return False 

with PlaylistSession("Road Trip") as pl: #=== Playing: Road Trip ===
    pl.add(Track("T01", "Bohemian Rhapsody", "Rock", 354)) #[T01] Bohemian Rhapsody (Rock, 354s) -> QUEUED
    pl.add(Track("T02", "Blinding Lights", "Pop", 200)) #[T02] Blinding Lights (Pop, 200s) -> QUEUED
    pl.add(Track("T03", "Clair de Lune", "Classical", 330)) #[T03] Clair de Lune (Classical, 330s) -> SKIPPED

    for line in pl.filter(("Rock", "Pop")):
        print(line)
# Summary: 2 queued, 1 skipped
    print(pl._tracks[0] > pl._tracks[1])
#True
print()
#=== Stopped: Road Trip (3 tracks) ===
with PlaylistSession("Study Session") as pl: #=== Playing: Study Session ===
    pl.add(Track("T04", "White Noise", "Ambient", -60))

#!!! Error: Invalid duration for T04
#=== Stopped: Study Session (0 tracks) ===


    
        
    








    

        




