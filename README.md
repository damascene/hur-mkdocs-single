# Hur Freelancer MKdocs Material - Single Site

You are a freelancer? With Hur you are free again. You can create your own personalized website that is programmatically processable by indexers and directory services. You create a toml file with your data and the reset is on this tool.

This website is a part of the Hur project which includes multiple tools to create profile, represent it and create a directory.

## Create Your Site

To create your own static site to show your services and provide it to the world do the following:

1. Fork this repository
  1. If you want it to be the main website name it ("github_username.github.io")
2. Change `site_name:` in `mkdocs.yml`
3. rename `docs/toml/com.gitlab.example_user.toml` file to your own username.
  * if your gitlab username is my_user you name the file `com.gitlab.my_user.toml`
4. From Gitlab left panel go to Deploy > Pages, there:
  1. Check _Force HTTPS (requires valid certificates)_
  2. Uncheck _Use unique domain_

This should be it.


## Hints

### Creating TOML profile

To generate your own data you can use the profile generation tool at:
https://hur-project.gitlab.io/hur-frontend-sveltekit/

### Style and Customization 

This software is based on Material for MkDocs. It has many style and customization options

https://squidfunk.github.io/mkdocs-material/


## License

Licensed under AGPL-V3 for entities that block knowledge by licensing, For other human beings it's open.
