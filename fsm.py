from transitions.extensions import GraphMachine
from bs4 import BeautifulSoup
import telegram
import urllib
import random

class TocMachine(GraphMachine):

    global x

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_help(self, update):
        text = update.message.text
        return text.lower() == 'help'
    
    def is_going_to_garbage(self, update):
        text = update.message.text
        return text.lower() != 'help' and text.lower() != 'search'
    
    def is_going_to_search(self, update):
        text = update.message.text
        return text.lower() == 'search'
    
    def is_going_to_table(self, update):
        text = update.message.text
        return text.lower() == '賽程表'
   
    def is_going_to_team(self, update):
        text = update.message.text
        return text.lower() == '所有隊伍'

    def is_going_to_photo(self, update):
        text = update.message.text
        return text.lower() == '相片集'
    
    def is_going_to_result(self, update):
        text = update.message.text
        return text.lower() == '戰績'
    
    def is_going_to_intro(self, update):
        text = update.message.text
        if text.lower()=='簡介':
            return True
        elif text.lower()=='search' or text.lower()=="" or text.lower()=='返回' or text.lower()=='球隊介紹' or text.lower()=='所有球員' or text.lower() == '1' or text.lower()=='2' or text=='3' or text.lower()=='4' or text.lower()=='5' or text.lower()=='6' or text=='7' or text.lower()=='8' or text.lower()=='9' or text.lower()=='10' or text.lower() == '11' or text.lower()=='12' or text.lower()=='13' or text.lower()=='14' or text.lower()=='15' or text.lower()=='16' or text=='17' or text.lower()=='18' or text.lower()=='19' or text.lower()=='20':
            return False
        else:
            update.message.reply_text("你是不是累了啊XD那來聽個笑話吧")
            update.message.reply_text("小明：現在的手機電腦都流行觸屏,科技發展速度太快了,說不定哪天電視都觸屏了\n小新：你傻阿！有遙控器不用,非要走過去用手指戳？")
    
    def is_going_to_member(self, update):
        text = update.message.text
        if text.lower()=='返回' or text.lower() == '所有球員' or text.lower()=='球隊介紹':
            return True
        elif text.lower() == '台電女排' or text.lower()=='中國人纖' or text=='ATTACKLINE' or text.lower()=='匯竑國際' or text.lower()=='台電男排' or text.lower()=='國訓中心' or text=='MIZUNO' or text.lower()=='長力育樂' or text.lower()=='桃園石易':
            return False
        else:
            update.message.reply_text("別再亂輸入了唷,不然柯P要生氣了")
            update.message.reply_photo(photo="http://twama.tw/img_tshirt/1422708559.png")
    
    def is_going_to_content(self, update):
        text = update.message.text
        if  text.lower()=='返回' or text.lower() == '台電女排' or text.lower()=='中國人纖' or text=='ATTACKLINE' or text.lower()=='匯竑國際' or text.lower()=='台電男排' or text.lower()=='國訓中心' or text=='MIZUNO' or text.lower()=='長力育樂' or text.lower()=='桃園石易':
            return True
        elif text.lower()=='所有隊伍':
            return False
        else:
            update.message.reply_text("沒有這個隊伍喔！再選擇一次吧")
            update.message.reply_photo(photo="http://blog.xuite.net/im3066/haikyu/393542990/cover600.jpg")
    
    def is_going_to_number(self, update):
        text = update.message.text
        if  text.lower()=='返回' or text.lower() == '1' or text.lower()=='2' or text=='3' or text.lower()=='4' or text.lower()=='5' or text.lower()=='6' or text=='7' or text.lower()=='8' or text.lower()=='9' or text.lower()=='10' or text.lower() == '11' or text.lower()=='12' or text.lower()=='13' or text.lower()=='14' or text.lower()=='15' or text.lower()=='16' or text=='17' or text.lower()=='18' or text.lower()=='19' or text.lower()=='20':
            return True
        elif text.lower()=='相片集':
            return False
        else:
            update.message.reply_text("只能選1~20喔,別超過")
            update.message.reply_photo(photo="http://bbs.creaders.net/upfile/images/20170311/20170311105135_40698.jpg")

    def on_enter_help(self, update):
        update.message.reply_text("輸入「search」來查詢吧\n或是輸入「返回」都可以回主畫面喔\n不然亂輸入你就知道會怎麼樣了")
        self.go_back(update)

    def on_exit_help(self, update):
        print('Leaving help')

    def on_enter_search(self, update):
        keyboard=[['簡介'],['所有隊伍'],['賽程表'],['戰績'],["相片集"]]
        update.message.reply_text("請點選或是輸入以下想要知道的項目",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        self.advance(update)

    def on_exit_search(self, update):
        print('Leaving search')

    def on_enter_garbage(self, update):        
        num=random.randint(0,3)
        if num==0:
            update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108230.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")
        elif num==1:
            update.message.reply_photo(photo="https://scontent.ftpe8-4.fna.fbcdn.net/v/t1.0-9/22554767_819971908175921_8942796579020062721_n.jpg?oh=37351512c5da0dc5694bc388eeee6c81&oe=5ABCCA3C")
        elif num==2:
            update.message.reply_photo(photo="https://scontent.ftpe8-4.fna.fbcdn.net/v/t1.0-9/22007769_675866442624169_963119946493725916_n.jpg?oh=a5f0f4fac42680fd7ef42b8b2af37011&oe=5AB20647")
        elif num==3:
            update.message.reply_text("來聽聽皮卡丘打排球的音效,休息一下吧")
            update.message.reply_audio(audio=open('volleyball.mp3','rb'))
        update.message.reply_text("快輸入「search」來獲取更多資料吧")
        self.go_back(update)

    def on_exit_garbage(self, update):
        print('Leaving garbage')

    def on_enter_intro(self, update):
        update.message.reply_text("106企業十三年甲級男女排球聯賽") 
        update.message.reply_text("官網：http://tvl.ctvba.org.tw/") 
        update.message.reply_text("FB：https://www.facebook.com/CTVBA888/") 
        update.message.reply_text("直播：http://video.foxsports.com.tw/")
        update.message.text=""
        self.go_back(update)

    def on_exit_intro(self, update):
        print('Leaving intro')

    def on_enter_table(self, update):
        update.message.reply_text("賽程表：http://tvl.ctvba.org.tw/fixtures-results/") 
        update.message.text=""
        self.go_back(update)

    def on_exit_table(self, update):
        print('Leaving table')

    def on_enter_photo(self, update):
        keyboard=[['1','2','3','4','5'],['6','7','8','9','10'],['11','12','13','14','15'],['16','17','18','19','20']]
        update.message.reply_text("請點選或是輸入1~20來查看照片吧",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        self.advance(update)

    def on_exit_photo(self, update):
        print('Leaving photo')

    def on_enter_team(self, update):
        keyboard=[['台電女排','中國人纖'],['ATTACKLINE','匯竑國際'],['台電男排','國訓中心'],['MIZUNO','長力育樂','桃園石易']]
        update.message.reply_text("喜歡哪一個隊伍啊",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        self.advance(update)

    def on_exit_team(self, update):
        print('Leaving team')
    
    def on_enter_content(self, update):
        global x
        text=update.message.text
        if text=='台電女排':
            x='1'
        if text=='ATTACKLINE':
            x='2'
        if text=='中國人纖':
            x='3'
        if text=='匯竑國際':
            x='4'
        if text=='台電男排':
            x='5'
        if text=='MIZUNO':
            x='6'
        if text=='長力育樂':
            x='7'
        if text=='桃園石易':
            x='8'
        if text=='國訓中心':
            x='9'
        if text !='返回':
            keyboard=[['球隊介紹'],['所有球員']]
            update.message.reply_text("想要知道哪一個呢？？",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
            self.advance(update)
        else:
            self.go_back(update)

    def on_exit_content(self, update):
        print('Leaving content')

    def on_enter_number(self, update):
        text=update.message.text
        if text=='1':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_a87a34be665c9f10c4f804cf83118158.jpg")
        if text=='2':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_1a63ac02fc5f7094e4555b672545a9cd.jpg")
        if text=='3':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_a765f434e241fbe0b7aa20a1e8b69791.jpg")
        if text=='4':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_b557934ddefb92da055f722d7d819f19.jpg")
        if text=='5':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_13cfd09d57e6823fa92be9d91149a6a1.jpg")
        if text=='6':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_c809371337c420b22ccaa7840e6605a4.jpg")
        if text=='7':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_2051e4b2fb634501d1183594564b8019.jpg")
        if text=='8':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_478170b98cdf36fe9723b33c0efc4fce.jpg")
        if text=='9':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_d1c44d1c7e5eae1f34831738afb5792a.jpg")
        if text=='10':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_f19d81cbfd3b6014926335e4f553907f.jpg")
        if text=='11':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_14464cc94e00e534bf51bf880837756f.jpg")
        if text=='12':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_045a02e5f474e671db7823cb3d99d854.jpg")
        if text=='13':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_391bcd4b6cafadfd203ad366aec597a1.jpg")
        if text=='14':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_5857f0eb9c7e77637a32afbc48804dde.jpg")
        if text=='15':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_f9128ffda6ccb1e739e7c8e1e93d2e38.jpg")
        if text=='16':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_af59ca8adadd8a9ea3bbdfec092f94fd.jpg")
        if text=='17':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_f01cf55ab70673159a4ecfd0fb24a6b0.jpg")
        if text=='18':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_87edcaf692f8c40daa45d3d416d0c9b0.jpg")
        if text=='19':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_bcc21a1cd239458f76c6dee9b6a94f01.jpg")
        if text=='20':
            update.message.reply_photo(photo="https://d2p1ovod81kcns.cloudfront.net/600_27909bd593f8eed78a781cd95f092e56.jpg")
        self.go_back(update)

    def on_enter_result(self, update):
        update.message.reply_text("戰績：http://tvl.ctvba.org.tw/league-table/")
        update.message.text=""
        self.go_back(update)

    def on_exit_result(self, update):
        print('Leaving result')
    
    def on_enter_member(self, update):
        global x
        text=update.message.text        
        if text=='球隊介紹':           
            update.message.reply_text("多了解這個球隊吧！",reply_markup=telegram.ReplyKeyboardRemove())
            if x=='1':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108223.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")                       
            if x=='3':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108225.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='2':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108226.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='4':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108232.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='5':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108231.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='6':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108229.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='7':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108224.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='8':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108227.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
            if x=='9':
                update.message.reply_photo(photo="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2017/10/12/realtime/4108228.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600")       
        if text=='所有球員':
            update.message.reply_text("請點選想要了解的球員",reply_markup=telegram.ReplyKeyboardRemove())
            if x=='1':
                url="http://tvl.ctvba.org.tw/team/%e5%8f%b0%e9%9b%bb/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-166')
                num=["李姿瑩","","張秝芸","","黃瀞萱","","曾琬羚","","黃芯瑜","","溫憶慈","","陳㬢","","謝苡臻","","張妤嘉","","李淯","","郭靚儀","","楊孟樺",""]
        
            if x=='2':
                url="http://tvl.ctvba.org.tw/team/%e7%8f%80%e5%85%86/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-168')
                num=["艾萊莎","","蕭湘凌","","譚緹","","柯粢薰","","畢雯媛","","蔡沁瑤","","魏璽格","","吳秀玲","","陳佳蔓","","吳靜婷","","余金鳳","","丁柔安",""]
            
            if x=='3':
                url="http://tvl.ctvba.org.tw/team/%e4%b8%ad%e7%ba%96/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-167')
                num=["張瓈文","","羅儀璟","","陳姿雅","","吳韋華","","劉美菁","","王艾仕","","邱雅惠","","廖苡任","","蕭憶玲","","陳莞婷","","賴湘程","","簡佳惠",""]
            
            if x=='4':
                url="http://tvl.ctvba.org.tw/team/%e5%8c%af%e7%ab%91/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-169')
                num=["童琪芳","","陳昱潔","","張嘉羚","","黃蔓亞","","劉雙菱","","溫以勤","","蔡依琳","","劉煜淳","","黃情維","","林書荷","","鍾乙禎","","鄭語倢",""]
            
            if x=='5':
                url="http://tvl.ctvba.org.tw/team/taipower/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-43')
                num=["陳保宏","","黃建逢","","張善源","","莊邵捷","","顏振富","","林宜暉","","戴儒謙","","王前鑌","","詹旻翰","","江天祐","","王明浚","","李佳軒",""]
            
            if x=='6':
                url="http://tvl.ctvba.org.tw/team/mizuno/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-34')
                num=["謝雅仁","","黃祥源","","高偉誠","","鄭旭辰","","黃正良","","伍政廷","","陳昱翰","","林國鈞","","李明穎","","吳宗軒","","李興國","","蘇厚禎",""]
       
            if x=='7':
                url="http://tvl.ctvba.org.tw/team/%e9%95%b7%e5%8a%9b/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-165')
                num=["黃世豪","","莊明叡","","潘均儒","","黃士展","","焦睿誠","","林政揚","","吳政陽","","林鉻惟","","黃韋程","","盧清銓","","林志勇","","阮柏勳",""]
            
            if x=='8':
                url="http://tvl.ctvba.org.tw/team/%e7%9f%b3%e6%98%93%e7%aa%af%e6%a5%ad%e8%82%a1%e4%bb%bd%e6%9c%89%e9%99%90%e5%85%ac%e5%8f%b8-%e7%9f%b3%e6%98%93%e7%94%b7%e6%8e%92/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-339')
                num=["曾弘仁","","黃建銘","","陳哲明","","黃文彥","","陳顥文","","陳偉綸","","陳政綺","","黃鈞璟","","石修智","","李東儒","","洪熙鈞","","鄭玉森",""]
            
            if x=='9':
                url="http://tvl.ctvba.org.tw/team/%e5%9c%8b%e8%a8%93/"
                page=urllib.request.urlopen(url)
                soup=BeautifulSoup(page,"html.parser")
                divs=soup.find('article',id='post-45')
                num=["劉鴻敏","","許美中","","潘柏鋐","","劉鴻杰","","劉育齊","","張良皓","","林元魏","","黃宇晨","","陳嘉榆","","甘明修","","羅偉哲","","董力憶",""]
            c=0
            choose=[]
            name="[{}]({})"
            for tds in divs.find_all('a',href=True):                
                if c%2==0:
                    choose.append(name.format(num[c],tds['href']))
                c=c+1
            update.message.reply_text('\n'.join(str(l) for l in choose),parse_mode=telegram.ParseMode.MARKDOWN)
        self.go_back(update)

    def on_exit_member(self, update):
        print('Leaving member')
    
