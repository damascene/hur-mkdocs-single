import tomli
import snakemd
import logging
from pathlib import Path
import sys
import glob
import os

from helpers import extract_domain, url_logo_dict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)  # INFO - DEBUG

i18n_toml = Path(__file__).parent / "i18n.toml"

latest_format_version = "0.1.1"

generator = "mkdocs-material"


try:
    logger.debug(sys.argv[1])
    logger.debug(sys.argv[2])
    if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
        pass
    else:
        exit("No source or destination directory provided")
except Exception as e:
    raise e
    exit("Unable to read sys arguments")

# Get list of files in the source directory
toml_file_list = glob.glob(f"{sys.argv[1]}/*.toml")
logger.debug(f"toml file list: {toml_file_list}")


def import_translation(i18n_toml):
    with open(i18n_toml, "rb") as f:
        return tomli.load(f)
        logger.debug(f"i18n_dict: {lang}")


lang = import_translation(i18n_toml)


def load_toml(toml_file):
    with open(toml_file, "rb") as f:
        logger.debug(f"loading toml file: {toml_file}")
        return tomli.load(f)

    # New File will remove last 4 characters from file name to remove
    # `.toml` suffix


def check_language(toml_dict):
    try:
        toml_dict["لغة_الملف"]
        return "ar"
        logger.debug(f"File language is Arabic")
    except:
        if "file_language" in toml_dict:
            if toml_dict["file_language"] == "en":
                return "en"
                logger.debug(f"File language is English")
            else:
                return toml_dict["file_language"]
        else:
            return "en"
            logger.debug(f"File language is not recognized or missing")


def create_markdown(toml_dict, toml_file, file_language):
    logger.debug(f"Working on {toml_file}")
    doc = snakemd.new_doc()
    data = lang[file_language]["data"]
    website = lang[file_language]["website"]
    name = lang[file_language]["name"]
    services = lang[file_language]["services"]
    description = lang[file_language]["description"]
    contact_accounts = lang[file_language]["contact_accounts"]
    websites = lang[file_language]["websites"]
    tags = lang[file_language]["tags"]
    skills = lang[file_language]["skills"]
    contact_accounts_title = lang[file_language]["contact_accounts_title"]
    services_of = lang[file_language]["services_of"]
    category = lang[file_language]["category"]
    sub_category = lang[file_language]["sub_category"]
    service_image = lang[file_language]["service_image"]
    title = lang[file_language]["title"]
    price = lang[file_language]["price"]
    hourly_rate = lang[file_language]["hourly_rate"]
    user_description = lang[file_language]["user_description"]
    profile_image = lang[file_language]["profile_image"]

    name = toml_dict[data][name]

    page_title = name

    site_list = []
    contact_methods = []
    user_services = []

    file_format = lang[file_language]["file_format"]

    if file_format in toml_dict:
        pass
    else:
        toml_dict[file_format] = latest_format_version
        logger.debug(f"Setting non specified file version to latest")

    if toml_dict[file_format] == "0.1.1":
        hourly_rate = toml_dict[data][hourly_rate]
        profile_image = toml_dict[data][profile_image]
        user_description = toml_dict[data][user_description]
        user_skills = toml_dict[tags]
        logger.debug(f"Handling version 0.1.1")
        catigories = ",".join(user_services)

        for i in toml_dict[services]:
            user_services.append(i["category"])

        if generator == "pelican":
            catigories = ",".join(user_services)
            skill_tags = ",".join(user_skills)

            doc.add_paragraph(f"Title: {name}")
            doc.add_paragraph(f"Category: {catigories}")
            doc.add_paragraph(f"Tags: {skill_tags}")

        elif generator == "mkdocs-material":
            # mkdocs does not have catigories so we use tags only
            
            # Generate tags for mkdocs-material
            tags = "---\ntags:\n  - "+"\n  - ".join(user_skills)+"\n---"
            print(tags)
            doc.add_raw(tags)

            doc.add_paragraph(f"# {name}")  # Page name takes top head so we set it

                
        # ~ doc.add_paragraph(f"![{i[title]}]({profile_image})")
        # Allow Markdown in user description
        doc.add_raw(user_description)

        doc.add_paragraph(f"**Hourly Rate: {hourly_rate}** 💰")

        doc.add_heading(f"{services_of} {name}")

        for i in toml_dict[services]:
            user_services.append(i)
            doc.add_heading(i[title], 2)

            for images in i[service_image]:
                doc.add_paragraph(f"![{i[title]}]({images})")

            # ~ second_heading = i[category] +" - "+ i[sub_category]
            # ~ doc.add_heading(second_heading, 2)

            # Allow Markdown in service description
            doc.add_raw(i[description])
            doc.add_paragraph(f"**Service price: {str(i[price])}** 💰")

            doc.add_horizontal_rule()

        for i in toml_dict[data][website]:
            website_link = i["text"]
            domain = extract_domain(website_link)
            try:
                logo = url_logo_dict[domain]
            except:
                logo = ""
                
            site_list.append(f"{logo} [{website_link}]({website_link})")

        logger.debug(f"site_list {site_list}")

        doc.add_heading(websites, 2)
        doc.add_unordered_list(site_list)

        file_name_stem = Path(toml_file).stem

        if generator == "pelican":
            doc.add_raw(f":simple-toml: <a id='toml_file' href='toml/{file_name_stem}.toml'>Toml file!</a>")
        elif generator == "mkdocs-material":
            doc.add_raw(f":simple-toml: <a id='toml_file' href='../toml/{file_name_stem}.toml'>Toml file!</a>")
        
        doc.add_raw(f"`file format: {toml_dict['file_format']}`")

        # ~ doc.add_heading(contact_accounts_title, 3)
        # ~ doc.add_unordered_list(contact_methods)

        # ~ doc.output_page(dump_dir="/home/blank/dev/gitlab/hur/freelancers/")

        doc.dump(f"{sys.argv[2]}/{file_name_stem}")
    else:
        logger.error(f"Fileformat is not supported")
        raise("Fileformat is not supported")


for i in toml_file_list:
    toml_dict = load_toml(i)
    file_language = check_language(toml_dict)
    create_markdown(toml_dict, i, file_language)
    logger.info(f"Creating Markdown for {i}")


def remove_extra_line(markdown_file):
    with open(markdown_file) as inputfile:
        lines = inputfile.read()

    lines = lines.replace("\n\nCategory", "\nCategory")
    lines = lines.replace("\n\nTags", "\nTags")
    logger.info(f"removed extra lines in {markdown_file}")

    with open(markdown_file, "w") as f:
        for line in lines:
            f.write(line)


markdown_file_list = glob.glob(f"{sys.argv[2]}/*.md")

# ~ for i in markdown_file_list:
    # ~ remove_extra_line(i)
