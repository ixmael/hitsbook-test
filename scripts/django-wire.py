import json
from pprint import pprint

if __name__ == "__main__":
  css = []
  js  = []

  webpack = None
  with open('webpack-stats.json', 'r') as webpack_stats:
    webpack = json.load(webpack_stats)
  
  if webpack:
    if webpack['status'] == 'done':
      for chunk in webpack['chunks']['hitsbook']:
        if (chunk['name'].endswith('.css')):
          css.append('<link rel="stylesheet" href="{{% static \'/{}\' %}}">'.format(chunk['name']))
        
        if (chunk['name'].endswith('.js')):
          js.append('<script src="{{% static \'/{}\' %}}"></script>'.format(chunk['name']))
  
  with open('./server-app/templates/_css.html', 'w') as css_file:
    css_file.write('{% load static %}\n')
    css_file.write('\n'.join(css))
    css_file.write('\n')
  
  with open('./server-app/templates/_js.html', 'w') as js_file:
    js_file.write('{% load static %}\n')
    js_file.write('\n'.join(js))
    js_file.write('\n')

