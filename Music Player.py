
print('Welcome To Music Player!!\n')
print('We Have Arijit Singh Hit Songs\n')
music_list={'kesariya':'C:\\Users\\KIIT\\Downloads\Kesariya_Brahmāstra___Ranbir_Kapoor___Alia_Bhatt.mp3',
            'apna bana le':'C:\Users\KIIT\Downloads\Apna-Bana-Le(PagalWorld).mp3',
            'agar tum saath ho':'C:\Users\KIIT\Downloads\Agar Tum Saath Ho_64(PagalWorld.com.se).mp3'}
music= input('Please Enter The Name Of The Song You Want To Listen!\n')
from playsound import playsound
if(music=='kesariya'):
    print('You Are Listening Kesariya\n')
    playsound('C:\\Users\\KIIT\\Downloads\Kesariya_Brahmāstra___Ranbir_Kapoor___Alia_Bhatt.mp3')
elif(music=='apna bana le'):
    print('You Are Listening Apna Bana Le\n')
    playsound('C:\Users\KIIT\Downloads\Apna-Bana-Le(PagalWorld).mp3')
elif(music=='agar tum saath ho'):
    print('You Are Listening Agar Tum Saath Ho\n')
     playsound('C:\Users\KIIT\Downloads\Agar Tum Saath Ho_64(PagalWorld.com.se).mp3')
else:
     print('Invalid Entry')