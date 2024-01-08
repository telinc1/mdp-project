import streamlit as st
import redis
import os

r = redis.Redis(host=os.environ["REDIS_HOST"])

if 'question' in st.session_state:
    st.text('Which two words traditionally appear onscreen at the termination of a feature film?')

    for ans in ('The End', 'The Conclusion', 'The Finish', 'The Pizza Rolls Are Done'):
        if st.button(ans):
            r.publish('wwtbam', f'''ANSWER {st.session_state['question']} {ans}''')

    st.stop()

pubsub = r.pubsub()
pubsub.subscribe('wwtbam')

for message in pubsub.listen():
    if message['type'] == 'message':
        msg = message['data'].decode('utf-8')

        if msg.startswith('START_GAME'):
            st.session_state['question'] = msg.split(' ')[1]
            st.rerun()
