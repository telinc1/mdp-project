import streamlit as st
import os
import redis

if 'username' in st.session_state:
    st.write(f'''Welcome, {st.session_state['username']}!''')

    r = redis.Redis(host=os.environ["REDIS_HOST"])

    if st.button('Start game'):
        r.publish('wwtbam', f'''START_GAME {st.session_state['username']}''')

        pubsub = r.pubsub()
        pubsub.subscribe('wwtbam')

        for message in pubsub.listen():
            if message['type'] == 'message':
                msg = message['data'].decode('utf-8')

                if msg.startswith('ANSWER'):
                    st.text(msg)
else:
    st.write('Welcome!')
