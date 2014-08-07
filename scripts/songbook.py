#!/usr/bin/python
# -*- coding: utf-8 -*- 

## Documentation for file
#
# More details. 
#
# @file songbook.py
# @author cuto <Jakub.Cuth@cern.ch>
# @date 2014-08-06

import os,shutil


class songbook:
    def __init__(s):
        s.data_path = "./data/"
        pass

    def filebasename(s, author, songname):
        return s.data_path+author.replace(" ","_") + "-"+songname.replace(" ","_")

    def get_listofsong_fromdir(s,directory):
        snglist=list()
        # list all files 
        for f in os.listdir(directory):
            # cut out the sufix
            fb = ".".join(f.split(".")[:-1])
            # uniq
            if fb not in snglist :
                snglist.append(fb)
        # sort
        snglist.sort()
        return snglist

    TEMPLATE_INDEX="""<!DOCTYPE html>
<html>
<body>

<h1>Seznam skladeb</h1>

<ul>
LIST
</ul>

</body>
</html>
    """

    def make_indexpage(s, outputdir, songlist):
        listtext=""
        for sng in songlist:
            listtext+="<li><a href=\"song/"
            listtext+=sng
            listtext+=".html\">"
            listtext+=sng
            listtext+="</a></li>\n"
            pass
        f = open(outputdir+"index.html","w")
        f.write(s.TEMPLATE_INDEX.replace("LIST",listtext))
        f.close()

    TEMPLATE_SONG="""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> {0} </title>
</head>
<body>

<h1>{0}</h1>

<p> <a href="{2}">open</a> <a href="../index.html">back</a> </p>
<audio controls>
  <source src="{2}" type="audio/mpeg" >
  Your browser does not support audio element.
</audio>
<pre style="font-size:14pt;">{1}</pre>


</body>
</html>
"""

    def make_songpage(s,outputdir,songname):
        name = songname.replace("_"," ").replace("-"," - ")
        with open(s.data_path+songname+".lyr","r") as f :
            lyrics=f.read()
        mp3link="../data/"+songname+".mp3"
        html = s.TEMPLATE_SONG.format(name,lyrics,mp3link)
        f = open(outputdir+songname+".html","w")
        f.write(html)
        f.close()
        pass

    def youtube2mp3(s,outputdir,songname):
        query ="""youtube-dl -o "{0}.%(ext)s" --extract-audio --audio-format mp3 {1}"""
        outmp3path=outputdir+songname
        with open(s.data_path+songname+".yt","r") as f :
            ytlink=f.read()
        os.path.exists(outmp3path) and os.remove(outmp3path)
        os.system(query.format(outmp3path,ytlink))
        pass





    def SetDataDir(s,datadir) :
        s.data_path = datadir

    def AddSong_youtube(s,author,songname,link):
        f = open (s.filebasename(author,songname)+".yt",'w')
        f.write(link)
        f.close()

    def AddSong_lyrics(s,author,songname,lyrics):
        f = open (s.filebasename(author,songname)+".lyr",'w')
        f.write(lyrics)
        f.close()

    def AddSong_youtube_lyrics(s,author,songname,link,lyrics):
        s.AddSong_youtube(author,songname,link)
        s.AddSong_lyrics(author,songname,lyrics)

    def AddSong_youtube_lyrics_list(s,ultimlist):
        for sng in ultimlist:
            s.AddSong_youtube_lyrics(sng[0],sng[1],sng[2],sng[3])

    def MakeHTML_karaoke(s,outputdir):
        # get list of songs from direcotory
        songlist = s.get_listofsong_fromdir(s.data_path)

        # make out dir
        shutil.rmtree(outputdir)
        os.makedirs(outputdir)
        os.makedirs(outputdir+"/song/")
        os.makedirs(outputdir+"/data/")
        # make index.html with list
        s.make_indexpage(outputdir,songlist)
        # make song pages
        for sng in songlist:
            s.youtube2mp3(outputdir+"/data/",sng)
            s.make_songpage(outputdir+"/song/",sng)



## Documentation for main
#
# Testing basic functionality
def main():

    sbk = songbook()

    # filling songbook
    sbk.SetDataDir("./data/")
    sbk.AddSong_youtube("Vlasta Redl", "Sbohem Galanecko", "https://www.youtube.com/watch?v=b2YdEwOKAdM")
    sbk.AddSong_lyrics("Vlasta Redl","Sbohem Galanecko",
"""
Sbohem, galánečko, já už musím jí - ti. 2x
Kyselé vínečko, kyselé vínečko
podalas' mi k pití. 2x

2. [:Sbohem, galánečko, rozlučme sa v pánu, :]
[:kyselé vínečko, kyselé vínečko
podalas' mi v džbánu. :]

3. [:Ač bylo kyselé, přeca sem sa opil, :]
[:eště včil sa stydím, eště včil sa stydím,
co sem všecko tropil, :]

4. [:Ale sa nehněvám, žes mňa ošidila, :]
[:to ta moja žízeň, to ta moja žízeň,
ta to zavinila. :]
""")


    # exporting songbook
    sbk.MakeHTML_karaoke("./output/html/")


    pass

if __name__ == '__main__' :
    main()
    pass

