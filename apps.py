from ranger.defaults.apps import CustomApplications as DefaultApps
from ranger.api.apps import tup

class CustomApplications(DefaultApps):

    def app_mplayer_playlist(self, c):
        return tup('mplayer', '-cache', '1024', '-cache-min', '30', '-playlist', *c)
        #return tup('mplayer', '-playlist', *c)

    def app_default(self, c):
        f = c.file

        if f.extension is not None:
            if f.extension in ('m3u', 'pls'):
                return self.app_mplayer_playlist(c)
            if f.extension in ('pdf', ):
                c.flags += 'd'
                return self.either(c, 'okular', 'xpdf', 'evince', 'zathura', 'apvlv')
            if f.extension in ('torrent', ):
                c.flags += 'd'
                return self.either(c, 'deluge')
            if f.extension in ('psd', 'xcf', ):
                c.flags += 'd'
                return self.either(c, 'gimp')
            if f.extension in ('pd', ):
                c.flags += 'd'
                return self.either(c, 'puredata')

        if f.image:
            return self.either(c, 'mirage', 'eog', 'feh')

        return DefaultApps.app_default(self, c)
