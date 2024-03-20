from datetime import datetime
from dateparser import parse as parse_dp
from dateutil.parser import parse as parse_du


class DateController:

    @staticmethod
    def date_conversion(date, is_french=False, debug=False):
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
            "janvier": "Jan",
            "Fevrier": "Feb",
            "Février": "Feb",
            "fevrier": "Feb",
            "février": "Feb",
            # "Mars": "Mar",
            # "mars": "Mar",
            "Avril": "Apr",
            "avril": "Apr",
            "Mai": "May",
            "mai": "May",
            "Juin": "Jun",
            "juin": "Jun",
            "Juillet": "Jul",
            "juillet": "Jul",
            "juil.": "Jul",
            "Aout": "Aug",
            "aout": "Aug",
            "Septembre": "Sep",
            "septembre": "Sep",
            "Octobre": "Oct",
            "octobre": "Oct",
            "Novembre": "Nov",
            "novembre": "Nov",
            "Decembre": "Dec",
            "Décembre": "Dec",
            "decembre": "Dec",
            "décembre": "Dec",
            # "Mercredi": ""
        }

        # Replace French words with English equivalents
        # for old, new in replacements.items():
        #     date = date.replace(old, new).strip()

        # Utiliser dateparser pour analyser la date
        if is_french:
            date_date = parse_dp(date)
        else:
            date_date = parse_du(date, dayfirst=True)

        if debug:
            print(f'\n\nAnnée = {date_date.year}')
            print('\nDate OK' if date_date.year > 1970 else '\nPROBLEME - Date FR')
            print(f'\nDate Finale = {date_date.strftime("%a, %d %b %Y %H:%M:%S GMT")}')

        # return date_date
        return date_date.strftime("%Y-%m-%d %H:%M:%S")  # return a string
        # return date
