import streamlit as st
from datetime import time, datetime
import time

st.title('欢迎访问自我关怀站点')
with st.expander('关于专栏'):
  st.image("https://qiniu.production.link3.cc/profile_images/1694315147716", width=100)
  st.markdown("**从今天起** ***自我关怀***")
  st.markdown("***专栏访问地址 link3.cc/zijiu***")
  st.markdown('''
    :red[保健意识] :orange[身心健康] :green[体育锻炼] :blue[健康饮食] :violet[生活方式]
    :gray[卫生习惯] :rainbow[保健食品].''')
  st.markdown(":tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

  multi = '''自我关怀是一种终生的习惯和文化，是个人为自己和家人保持健康而采取的行动'''
  st.markdown(multi)

st.header('自我关怀',divider='rainbow')

multi = '''
:tulip::cherry_blossom::tulip:自我关怀:tulip::cherry_blossom::tulip:

大多数人都相当健康，像孩子一样好。然而，随着年龄的增长，我们面临着生活中的挑战和诱惑，比如食物、酒精和烟草，以及久坐不动的生活方式。我们面临着选择和风险。

不幸的是，这些选择的共同结果——肥胖、缺乏身体活动、吸烟、酗酒和不健康饮食——是当今心脏病发作和中风、癌症、糖尿病、慢性呼吸系统疾病和其他“非传染性疾病”流行的原因。

好消息是，通过调整我们的生活方式，通过自我照顾来照顾自己，大大降低我们患这些疾病的风险是可能的。

自我照顾很难做到吗?有些因素当然是这样的，比如吸烟者很难戒烟。但我们大多数人都可以做很多事情来帮助自己保持健康，帮助预防或延缓生活方式引起的疾病。对我们大多数人来说，前进的道路是朝着积极的方向迈出一小步。


:sunflower::blossom::sunflower::blossom:Self-Care:sunflower::blossom::sunflower::blossom:

Most people are reasonably healthy and well as children. As we get older however, we are faced with the challenges and temptations of life such as food, alcohol and tobacco, and the opportunity for sedentary lifestyles. We are faced with choices, and risks.

Unfortunately the common result of these choices – obesity, physical inactivity, tobacco use, alcohol abuse and unhealthy diets – are the cause of today’s epidemic of heart attacks and strokes, cancers, diabetes, chronic respiratory disease and other ‘noncommunicable diseases.’

The good news is that it is possible to reduce substantially our risk of these diseases by adjusting our lifestyles, taking more care of ourselves by practicing self-care.

Is self-care hard to do? Some elements certainly are, such as the difficulty that smokers have in quitting tobacco use. But there is much that most of us can do to help ourselves to stay healthy and to help prevent or delay lifestyle diseases. The way forwards for most of us is to take small steps in positive directions.

'''
st.markdown(multi)

st.image("https://lirp.cdn-website.com/df8feb75/dms3rep/multi/opt/2-0fc4eb65-1920w.png", width=400)

st.header('自我关怀宣言', divider='rainbow')

multi = '''
自我保健是一套实用的、以人为本的活动，我们都应该采取这些活动来保持我们的健康和幸福。
自我照顾只能由个人自己承担，尽管更广阔的环境可以提供重要的帮助或存在重大的障碍。
自我照顾是每个人日常生活中很正常的一部分，无论他们的情况如何，都有意识或无意识地参与其中。
然而，在使自我保健更加明确和增强其在个人、家庭、社区和国家卫生方面的作用方面，仍有很大的潜力。

自我照顾既是一组活动，也是一个重复的行为循环(行动→监督→认识→评估→行动)。自我照顾行为涉及个人能力、机会和动机。

通过自我保健，人们可以更健康，并保持到老年，自己管理小病。
他们还可以更好地管理、延缓甚至预防所谓的“生活方式”疾病的出现，如心脏病、中风、糖尿病和许多癌症。

自我照顾并不意味着没有照顾，也不意味着人们只是在没有外界支持的情况下照顾自己。
相反，自我保健的总体目标是使人们摆脱对卫生专业人员和卫生系统的不必要依赖，使他们在获得适当支持、工具和知识的情况下能够更好地照顾自己。

自我保健对疾病预防和有疾病的人同样重要，因为自我保健的所有基本要素仍然需要进行，同时还需要针对疾病采取自我管理行动。

自我保健的主要受益者是自我照顾者，但其他受益者包括家庭成员和过度紧张的医疗保健系统。
在健康和保健权利与对自身健康和不良生活方式选择后果的责任之间，必须取得重要的社会平衡。

自我保健为所有利益相关者提供了巨大的机会，包括健康的个人和患者、政府、政策制定者、医疗保健专业人员、
社区组织、非政府组织、慈善机构、消费者组织和政府间组织。所有企业都关心员工的健康和福利，
有些企业在自我保健产品和服务方面有直接的商业利益。

在发达国家和资源贫乏的环境中，自我保健同样重要，尽管保健挑战的性质和自我保健的优先事项可能差别很大。
许多国家已将自我保健的各个方面纳入政策，并促进了一些创新和值得注意的做法。
然而，所有国家都距离实施旨在促进个人和人群自我保健能力、
转变专业做法或将卫生保健系统重新定位为预防性精神的有力和有意义的政策处方还有很长的路要走。
虽然实现有益健康模式的重要性已在理论上得到承认，联合国和世卫组织也发表了一些有益的全球言论，
但要实现真正的转变还有很长的路要走。

发展自我保健需要对证据、理论和实践进行系统的发展。
到目前为止，自我保健基本上处于当前卫生和社会系统的职权范围之外，没有得到学术界足够的研究和发展关注。
我们仍然缺乏确凿的证据来证明自我照顾的绝对必要性，以及在现实环境中实施自我照顾的最佳方式。
还有许多对自我保健很重要的活动“孤岛”，有很大的联系潜力。

促进自我保健有很大的机会和需要——向世界各地健康的个人、患者和所有利益攸关方阐明和促进自我保健的做法。
所有利益攸关方都将受益于普遍理解和接受的自我保健的统一全球战略发展，目前他们使用健康生活方式、自我管理或疾病预防等替代术语。
'''
st.markdown(multi)

col1, col2 = st.columns(2)
with col1:
  st.image("https://isfglobal.org/wp-content/uploads/2014/06/self-care-iceberg.jpg")
with col2:
  st.image("https://isfglobal.org/wp-content/uploads/2014/08/Screen-shot-2014-08-14-at-13.51.25.png")

st.caption(":blue[自我关怀是一种终生的习惯和文化，是个人为自己和家人保持健康而采取的行动] :sunglasses:")
tab1, tab2 = st.tabs(["思前", "想后"])

with tab1:
  if st.button('拥抱多姿多彩的生活!✨'):
    st.balloons()
    st.success('https://link3.cc/zijiu', icon="✅")

with tab2:  
  if st.button('行动!✨'):
    st.balloons()
    st.success('https://www.xiaohongshu.com/user/profile/64b71426000000001f0066a0', icon="✅")  
    



