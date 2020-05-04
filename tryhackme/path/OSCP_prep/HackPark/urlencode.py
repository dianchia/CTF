#!/usr/bin/python3

import urllib

f = {
'__VIEWSTATE': '9o3SmBZrJRQzfy7kkCOyg1NKfTXN9SunW5hHb0JM5r/ubhb/sUbr8XKtIkHyfD1mLN474Sg+pPuXWdMiqPAaX5eeuWiEmcjo/oRLYfMAEBQY7TmjTLJWpDM8pjhAtbQj0uT/eK+fW5Q5bWMVHOQJG1VsLSZk4UlrOHv0rfoxOl6M2svR',
'__EVENTVALIDATION': '/R+mdTL/GWcCAUXLZ/Hn36sbZ2AnlRTa1fQjpaUiDVremHkUfE/2wYoO+1H9E0WKYBtgbkGAfxjZX9etzDTsNtNchnNX5aRyrYyhc9kwC9IrsM/ZmOl5mQtb5UfhN36p7hpfAhJ5vR1ehq8TJreppnTAJqCO9Dhk7yfxQz7gDuzBqlcj',
'ctl00$MainContent$LoginUser$UserName':'admin',
'ctl00$MainContent$LoginUser$Password': '^PASS^',
'ctl00$MainContent$LoginUser$LoginButton': 'LoginButton'

}

print(urllib.urlencode(f))