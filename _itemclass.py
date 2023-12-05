from datetime import datetime
from dateparser import parse as parse_dp
from dateutil.parser import parse as parse_du
class MYNEWS:

    @staticmethod
    def DATE_Conversion(date, isFrench=None,dbg=False):
        replacements = {
            '&nbsp;': ' ',
            "il y a ": '',
            "minutes": 'minutes ago',
            "minute": 'minute ago',
            "minute agos ago": 'minutes ago',
            "heures": 'hours ago',
            "heure": 'hour ago',
            "jours": 'days ago',
            "jour": 'day ago',
            "Janvier": "Jan",
            "Fevrier": "Feb",
            "Février": "Feb",
            "Mars": "Mar",
            "Avril": "Apr",
            "Mai": "May",
            "Juin": "Jun",
            "Juillet": "Jul",
            "Aout": "Aug",
            "Septembre": "Sep",
            "Octobre": "Oct",
            "Novembre": "Nov",
            "Decembre": "Dec",
            "Décembre": "Dec",
            "janvier": "Jan",
            "fevrier": "Feb",
            "février": "Feb",
            "mars": "Mar",
            "avril": "Apr",
            "mai": "May",
            "juin": "Jun",
            "juillet": "Jul",
            "juil.": "Jul",
            "aout": "Aug",
            "septembre": "Sep",
            "octobre": "Oct",
            "novembre": "Nov",
            "decembre": "Dec",
            "décembre": "Dec"
        }

        # Replace French words with English equivalents
        for old, new in replacements.items():
            date = date.replace(old, new)

        # Utiliser dateparser pour analyser la date
        if not isFrench:
            date_date = parse_dp(date)
        else:
            date_date = parse_du(date, dayfirst=True)

        if dbg: 
            print(f'\n\nAnnée = {date_date.year}')
            print('\nDate OK' if date_date.year > 1970 else '\nPROBLEME - Date FR')
            print(f'\nDate Finale = {date_date.strftime("%a, %d %b %Y %H:%M:%S GMT")}')

        # return date_date
        return date_date.strftime("%Y-%m-%d %H:%M:%S")  # return a string