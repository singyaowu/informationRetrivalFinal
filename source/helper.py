last_names = set("陳林黃張李王吳劉蔡楊許鄭謝洪郭邱曾廖賴徐周葉蘇莊呂江何蕭羅高潘簡朱鍾彭游詹胡施沈余盧梁趙顏柯翁魏孫戴范方宋鄧杜傅侯曹薛丁卓馬阮董唐温藍蔣石古紀姚連馮歐程湯黄田康姜汪白鄒尤巫鐘黎涂龔嚴韓袁金童陸夏柳凃邵")

common_words = set(["馬上", "連結", "高調", "高雄", "高雄市","高市", "方式", "許多", "謝罪", "方向", "紀錄", "連鎖",
 "周一", "周二", "周三","白熱化", "周年","高雄人","", "周四","周五","周六","周日", "週一","週二", "週三", "週四", "週五", "週六", "週日", "周邊", "顏色", "金屬", "紀念", "連忙", "連身裙",
  "施政","施壓","高挑","金錢","白天","許可","尤以","高齡","蕭條","沈重","連日","高竿", "羅馬", "董事會","藍營","簡單","許許多多", "簡易",'嚴重', "嚴重性","高官","高於","高達","高樓","高額",
  "馬尾","高出","王子","黃色","藍色","連署書","陸續","高中","周圍","高效能", "曾經", "歐洲","馬來西亞", "陸軍","遊走","施行", "白皙", "金融", "夏日","方案","程度", "白紙", "藍綠", "高級",
  "白吃" "馬來西亞", "簡直", "高人氣", "馬路", "高速","施工","白色",'盧素梅',"陳弘志",'翁嫆琄','高峰會',"戴澤文",'楊凱婷','李清貴','周志豪',"高手","陸戰隊", '許久','林河名','施鴻基',"鄭鴻達",
  "石油","簡訊", "嚴重","嚴格","何哲欣","洪敬浤","林麒瑋","陳威叡","高漲",'金主', "嚴厲","馬習會","林彥臣","柳川","葉克膜","蘇怡璇","陳家祥","謝票","高昂","胡說","陳菊日","賴筱桐","藍淺","連鎖店",
  "劉星君","吳柏源","林姵妏","石化","曾品傑","杜拜", "杜微","謝曉星","曾珮瑛","", '簡體字','高興',"謝絕","謝謝","張貼","簡短","唐人", "金額", "游泳","林口","高度", "施放", "白宮","歐盟", "歐美",
   "白人","方針", "連播","高層","董事長","董事",'高市民調', "連署", "陸海","白皮書","藍天","程序","高喊", "蕭條","嚴苛", "高薪","鄭重","連任","紀念展", "陸委會", "尤其", "田徑", "田徑隊", "高血壓",
    "陸生", "陸客", "童裝", "連續", "連夜", "高學歷", "方面", "高等", "夏天", "方法", "顏值", "金字塔", '翁聿煌','陸網', '高齡化','丁丁','簡惠茹','連篇','洪池','何況', '白晝','吳亮儀'
    ])
include_words = set(["高雄"])
titles = set(["先生", "小姐","神","式","流","總","河",'陣營' "市長","委",'黑','語錄','坦言','姚人多','笑',"總召","醫","粉洗","粉","局長","屁","導", "妻", "處長","國","市府","表明","解釋", "總統", "董事長","案", "立委", "粉", "小弟弟", "小妹妹", "議員", "姓", "姓男子","姓男", "姓女", "男", "女","男妻子","女先生", "姓女子", "姓少年", "姓少女","婦", "老先生", "揆", "閣揆", "政府", "網友"])

special_cases = set(["川普","特朗普","普丁","梅克爾","阿諾", "杜特蒂","習近平", "石上", "石上優", "伊井野", "御子", "彌子", "伊井野御子", "伊井野彌子", "燕子學姐"])
def is_chinese(string):
    for chart in string:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False
    return True

def isName(term):
    if term in special_cases: return True
    if term in common_words: return False
    
    if len(term) < 2 or len(term) > 3 or (not is_chinese(term)):
        return False

    for word in include_words:
        if term in word or word in term:
            common_words.add(term)
            return False

    if term[0] in last_names:
        if term[1:] not in titles:
            special_cases.add(term)
            return True
    common_words.add(term)
    return False