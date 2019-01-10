"""Hass cmd."""


def breaking_change(url):
    """Create breaking_change list for HA."""
    import json
    import requests
    comp_base = 'https://www.home-assistant.io/components/'
    pull_base = 'https://github.com/home-assistant/home-assistant/pull/'
    url_data = requests.get(url).text.split('\n')
    raw_changes = []
    changes = {}
    changes['version'] = "0.{}.x".format(url[-2:])
    changes['data'] = []
    control = []
    for line in url_data:
        if "(breaking change)" in line:
            raw_changes.append(line)
    for change in raw_changes:
        if change[0:3] == '<p>':
            pass
        else:
            this = {}
            pull_request = str(change)
            pull = pull_request.split('home-assistant/home-assistant/pull/')[1]
            pull_request = pull.split('"')[0]
            if pull_request not in control:
                prlink = '{}{}'.format(pull_base, pull_request)
                try:
                    component = str(change)
                    component = component.split('(<a href="/components/')[1]
                    component = component.split('/">')[0]
                except:
                    component = ''
                doclink = '{}{}'.format(comp_base, component)
                desc = str(change).split('  <li>')[1]
                desc = desc.split('(<a ')[0]
                desc = desc.replace('</code>', '')
                desc = desc.replace('<code class="highlighter-rouge">', '')
                desc = desc.replace('\u2019', '`')
                desc = desc.replace('\u201c', '')
                desc = desc.replace('\u201d', '')
                this['pull_request'] = pull_request
                this['prlink'] = prlink
                this['component'] = component
                this['doclink'] = doclink
                this['description'] = desc
                changes['data'].append(this)
                control.append(pull_request)
    print(json.dumps(changes, sort_keys=True, indent=4, ensure_ascii=True))
