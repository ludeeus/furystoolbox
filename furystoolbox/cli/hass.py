"""Hass cmd."""


def breaking_change(number):
    """Create breaking_change list for HA."""
    import json
    import requests
    import os
    from github import Github
    from furystoolbox.common import share
    comp_base = 'https://www.home-assistant.io/components/'
    pull_base = 'https://github.com/home-assistant/home-assistant/pull/'
    github = Github(os.environ['GHTOKEN'])
    repo = github.get_repo('home-assistant/home-assistant.io')
    posts = repo.get_dir_contents('source/_posts', 'current')
    this_post = None
    for post in posts:
        if 'release' in post.path:
            name = post.path.split('/')[-1].split('.')[0]
            name = name.split('-')
            rel_number = name[-1]
            if rel_number == number:
                this_post = post.html_url
    if this_post is None:
        print("Release for", number, "not found")
        return
    url = this_post
    url_data = requests.get(url).text.split('\n')
    print(url)
    raw_changes = []
    changes = {}
    changes['version'] = "0.{}.x".format(url.split('.markdown')[0][-2:])
    changes['data'] = []
    control = []
    for line in url_data:
        if "(breaking change)" in line:
            raw_changes.append(line)
    for change in raw_changes:
        print(change)
        if change[0:3] == '<p>':
            pass
        else:
            this = {}
            try:
                pull = str(change)
                pull = pull.split('home-assistant/home-assistant/pull/')[1]
                pull = pull.split('"')[0]
            except:
                pull = None
            if pull not in control and pull is not None:
                prlink = '{}{}'.format(pull_base, pull)
                try:
                    split = '<a href="/home-assistant/home-assistant.io/blob/'
                    split += 'current/components/'
                    component = str(change)
                    component = component.split(split)[1]
                    component = component.split('">')[0]
                except:
                    component = None
                doclink = '{}{}'.format(comp_base, component)
                desc = str(change).split('<li>')[1]
                desc = desc.split('(<a ')[0]
                desc = desc.replace('</code>', '')
                desc = desc.replace('<code class="highlighter-rouge">', '')
                desc = desc.replace('\u2019', '`')
                desc = desc.replace('\u201c', '')
                desc = desc.replace('\u201d', '')
                this['pull_request'] = pull
                this['prlink'] = prlink
                this['component'] = component
                this['doclink'] = doclink
                this['description'] = desc
                changes['data'].append(this)
                control.append(pull)
    data = json.dumps(changes, sort_keys=True, indent=4, ensure_ascii=True)
    print(data)
    share(data)
    return changes
