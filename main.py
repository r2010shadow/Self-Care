import streamlit as st
from datetime import time, datetime
import time

st.title('欢迎访问')

with st.expander('关于自我关怀专栏'):
  st.image("https://qiniu.production.link3.cc/profile_images/1694315147716")
  st.markdown("*自我关怀* 从**今天** ***开始***.")
  st.markdown('''
    :red[保健意识] :orange[身心健康] :green[体育锻炼] :blue[健康饮食] :violet[生活方式]
    :gray[卫生习惯] :rainbow[保健食品].''')
  st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

  multi = '''
  告别无数个辗转反侧的夜晚，无数个心灰意冷与叹息
  想生活步入正轨，必须先振作自己
  今天起关怀自我
  link3.cc/zijiu
  '''
  st.markdown(multi)



