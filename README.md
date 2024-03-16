# Hur Freelancer MKdocs Material - Single Site

You are a freelancer? With Hur you are free again. You can create your own personalized website that is programmatically processable by indexers and directory services. You create a toml file with your data and the reset is on this tool.

This website is a part of the Hur project which includes multiple tools to create profile, represent it and create a directory.


## Prepare Your Data

To generate your profile you can use the profile generation tool at:
https://hur-project.gitlab.io/hur-frontend-sveltekit/

## Create Your Site

### Gitlab

To create your own static site to show your services and provide it to the world do the following:

1. Fork this repository 
    1. If you want it to be the main website name it ("github_username.github.io")
2. Change `site_name:` in `mkdocs.yml`
3. Rename `docs/toml/com.gitlab.example_user.toml` file to your own username.
    * if your gitlab username is _my_user_ you name the file `com.gitlab.my_user.toml`
4. Replace content of c file with profile data generated from the [profile tool](https://hur-project.gitlab.io/hur-frontend-sveltekit/).
5. From Gitlab left panel go to **Deploy** > **Pages**, there:
    1. Check _Force HTTPS (requires valid certificates)_
    2. Uncheck _Use unique domain_

Link to page will be there, Enjoy!

### Github

1. Fork this repository 
    1. If you want it to be the main website name it ("github_username.github.io")
1. Rename `docs/toml/com.gitlab.example_user.toml` file to your own username.
    * if your git repository username is _my_user_ in github you name the file `com.github.my_user.toml`
1. Replace content of the toml file with profile data generated from the [profile tool](https://hur-project.gitlab.io/hur-frontend-sveltekit/).
1. From Github top bar go to settings then from the left panel go to pages. in __Build and deployment__ section. Select __gh-pages__ then press the save button.
    1. Check _Force HTTPS (requires valid certificates)_
    1. Uncheck _Use unique domain_

Link to page will be there, Enjoy!


## Hints

### Change settings

You can change `site_name:` in `mkdocs.yml` among other configurations.

### Style and Customization 

This software is based on Material for MkDocs. It has many style and customization options

https://squidfunk.github.io/mkdocs-material/


## License

Licensed under AGPL-V3 for entities that block knowledge by licensing, For other human beings it's open.
