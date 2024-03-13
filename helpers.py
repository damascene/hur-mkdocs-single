from urllib.parse import urlparse

url_logo_dict = {
    "hub.docker.com" : ":fontawesome-brands-docker:",
    "www.youtube.com" : ":fontawesome-brands-youtube:",
    "youtube.com" : ":fontawesome-brands-youtube:",
    "www.twitter.com" : ":simple-twitter:",
    "www.x.com" : ":simple-x:",
    "matrix.org" : ":simple-matrix:",
    "matrix.to" : ":simple-matrix:",
    "youtu.be" : ":simple-youtube",
    "www.behance.net" : ":fontawesome-brands-behance:",
    "www.fiverr.com" : ":simple-fiverr:",
    "www.freelancer.com" : ":simple-freelancer:",
    "www.upwork.com" : ":simple-upwork:",
    "linktr.ee" : ":simple-linktree:",
    "t.me" : ":simple-telegram:",
}

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc
