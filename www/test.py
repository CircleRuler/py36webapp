#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm, asyncio, time
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop, user='root',password='password', db='awesome')
    for x in range(1,20):
        summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        content = '没有什么内容'
        user_id = '001490081368365d50bca6ec0064c0c9efb7e588a79de52000'
        user_name = 'xubeilei'
        user_image='http://www.gravatar.com/avatar/15dc614aa5b0188624bbaf4b4524dd10?d=mm&s=120'
        u = Blog(id=str(x), name='Test Blog'+str(x), summary=summary, content = content,user_id=user_id,user_name=user_name,user_image=user_image, created_at=time.time()-120)

        await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()