from django.shortcuts import render
import re
from .models import Subtitle
from django.utils import timezone

# Create your views here.
def input_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        subtitle_link = request.POST.get('subtitle')

        if subtitle_link:
            # Regular expression to extract YouTube video ID from the URL
            vid_regex = r'(?:youtube(?:-nocookie)?\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
            video_id_match = re.search(vid_regex, subtitle_link)

            if video_id_match:
                video_id = video_id_match.group(1)
                #video = Subtitle.objects.create(url=video_id, title=title)
                video = Subtitle(url=video_id, title=title, date=timezone.now()) # declarationsave data to the subtitle 
                print(video_id)
                video.save()#save the data
                return render(request, 'input_video.html', {'video': video})
            else:
                return render(request, 'input_video.html', {'message': 'Invalid YouTube URL'})
        else:
            return render(request, 'input_video.html', {'message': 'YouTube URL is required'})

    return render(request, 'input_video.html')

def home(request):
    video = Subtitle.objects.all()
    return render(request, 'index.html', {'video': video})
