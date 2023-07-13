# import sys
# srcpath = '/Users/orm/repos/mitaskem/src'
# askempath = '/Users/orm/repos/mitaskem'
# sys.path.append(askempath)
# sys.path.append(srcpath)

import os
import openai
from mitaskem.src.mit_extraction import async_mit_extraction_restAPI
import asyncio
import gpt_key

bucky_path = os.path.abspath('../../mitaskem/resources/models/Bucky/bucky.txt')
res = asyncio.run(async_mit_extraction_restAPI('/tmp/askemcache/bucky.txt', gpt_key=gpt_key.GPT_KEY , cache_dir='/tmp/askemcache/'))

print('result:', res)

