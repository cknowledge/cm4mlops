from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if not env.get('CM_DOWNLOAD_FILENAME'):
        urltail = os.path.basename(env['CM_DOWNLOAD_URL'])
        urlhead = os.path.dirname(env['CM_DOWNLOAD_URL'])
        if "." in urltail and "/" in urlhead:
            env['CM_DOWNLOAD_FILENAME'] = urltail
        else:
            env['CM_DOWNLOAD_FILENAME'] = "index.html"

    filename = env['CM_DOWNLOAD_FILENAME']
    env['CM_DOWNLOAD_DOWNLOADED_FILENAME'] = filename

    url = env['CM_DOWNLOAD_URL']
    extra_download_options = env.get('CM_DOWNLOAD_EXTRA_OPTIONS', '')

    if env['CM_DOWNLOAD_TOOL'] == "wget":
         env['CM_DOWNLOAD_CMD'] = f"wget -nc {extra_download_options} {url}"
    if env['CM_DOWNLOAD_TOOL'] == "curl":
        env['CM_DOWNLOAD_CMD'] = f"curl {extra_download_options} {url}"

    #verify checksum if file already present
    if env.get('CM_DOWNLOAD_CHECKSUM'):
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = "echo {} {} | md5sum -c".format(env.get('CM_DOWNLOAD_CHECKSUM'), env['CM_DOWNLOAD_FILENAME'])
    else:
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = ""

    filename = os.path.basename(env['CM_DOWNLOAD_FILENAME'])
    filepath = os.path.join(os.getcwd(), filename)
    env['CM_DOWNLOAD_DOWNLOADED_PATH'] = filepath

    return {'return':0}

def postprocess(i):

    env = i['env']

    filepath = env['CM_DOWNLOAD_DOWNLOADED_PATH']

    if not os.path.exists(filepath):
        return {'return':1, 'error': 'CM_DOWNLOAD_FILENAME is not set and CM_DOWNLOAD_URL given is not pointing to a file'}

    if env.get('CM_DOWNLOAD_FINAL_ENV_NAME'):
        env['CM_DOWNLOAD_FINAL_ENV_NAME'] = filename

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
