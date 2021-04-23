from PIL import Image

#if no left banner then set to 0
left_indent = 407

#right bound
right_indent = 0

#upper bound
startY=28

#make each line start at different point
line_diff=70

#relative path of background image, use gray if leave empty 
background_png=''

#only display operators with master skills
master_only = True


#don't change 
line = 0
cnt = 0
slot_width = 0
slot_height = 0
bg_width = 0
bg_height = 0
startX = left_indent
bg=''
current_class = ''
mcnt = [0,0,0,0]


def print_operator(op, sk):

    #check qualifications
    if ( sk['skill1'] + sk['skill2'] + sk['skill3'] <= 0 and master_only):
        return

    #debug
    # print(op['name'])
    print(sk['name'])


    #cnt
    mcnt[sk['skill1']]+=1
    mcnt[sk['skill2']]+=1
    mcnt[sk['skill3']]+=1


    # change position
    global startX, line, startY, bg
    if (startX + slot_width > bg.width - right_indent):
        line += 1
        startX = line * line_diff + left_indent
        startY += slot_height
    
    
    

    #load images
    img1=Image.open('resource/Slot - single - background.png')
    img2=Image.open('avatar/'+op['filename']+'_'+str(sk['costume'])+'.png')
    img3=Image.open('resource/Slot - single  精二+黑遮罩.png')
    img4=Image.open('resource/Akteam-rarity_'+ op['rare']+ '.png')
    img5=Image.open('resource/潜能'+str(sk['potential'])+'.png')
    img6=Image.open('resource/'+ str( (sk['level'] // 10) * 10 ) +'.png')
    img7=Image.open('resource/专精'+ str( sk['skill1'] ) +'.png')
    img8=Image.open('resource/专精'+ str( sk['skill2'] ) +'.png')
    img9=Image.open('resource/专精'+ str( sk['skill3'] ) +'.png')

    #adjust images

    #print(str(img2.width) + '  ' + str(img2.height))
    ratio = img2.height / img2.width 
    img2= img2.resize((135, int(135 * ratio)), Image.ANTIALIAS)



    #paste images
    bg.paste(img1,(startX,startY), mask=img1.split()[3])
    bg.paste(img2,(startX + 12 ,startY + 284 - img2.height), mask=img2)
    bg.paste(img3,(startX + 12 ,startY + 284 - img3.height), mask=img3)
    bg.paste(img4,(startX + 12 ,startY + 284 - img4.height), mask=img4)
    bg.paste(img5,(startX + 22 ,startY + 244), mask=img5)
    bg.paste(img6,(startX + 108 ,startY + 250), mask=img6)
    bg.paste(img7,(startX + 17 ,startY + 292), mask=img7)
    bg.paste(img8,(startX + 62 ,startY + 292), mask=img8)
    if (op['rare'] == '6'):
        bg.paste(img9,(startX + 107 ,startY + 292), mask=img9)


    
    startX += slot_width
    #print('\n')

def print_class(class_name):
    global startX, line, startY, bg
    if (startX + slot_width > bg.width - right_indent):
        line += 1
        startX = line * line_diff + left_indent
        startY += slot_height

    img1=Image.open('resource/职业_'+ class_name +'.png')
    bg.paste(img1,(startX,startY), mask=img1.split()[3])


    startX += slot_width


if __name__ == "__main__":



    with open('operators.txt', 'r', encoding='utf-8') as f:
        operator = eval ('[' + f.read() + ']')



    with open('skills.txt', 'r', encoding = 'utf-8') as f:
        skill = eval ('[' + f.read() + ']')


    
    num = 8
    for sk in skill:
        
        #顺便的
        if ( sk['skill1'] + sk['skill2'] + sk['skill3'] > 0 or not master_only): num += 1

        posclass = ''
        for op in operator: 
            if (sk['name'] == op['name']): posclass = op['class']
        
        sk['class'] = posclass

    skill = sorted(skill, key = lambda i: (i['class'], i['level']),reverse=True)
    print('num = '+str(num)+'\n')


    if (background_png != ''):
        bg = Image.open(background_png)
    else:
        bg = Image.new('RGBA', (5000, 1080), (49, 49, 49, 255))
    
    bg_height = bg.height
    bg_width = bg.width

    img0=Image.open('resource/Slot - single - background.png')
    slot_width = img0.width
    slot_height = img0.height




    for sk in skill:

        pos = ''
        for op in operator:
            if (op['name'] == sk['name']):
                pos = op
                #print("matched! :" + op['name']+ '\n')

        if ( current_class != pos['class']):
            current_class = pos['class']
            print_class(current_class)
        print_operator(pos, sk)



    print("专精数量： ")
    print(mcnt)
    bg.show()
    bg.convert('RGB').convert('RGBA').save('result-c.png')
    '''

 

    while (startY < bg.height - img0.height):
        startX=line_diff * line + left_indent

        while (startX < bg.width - img0.width):



            img1=Image.open('resource/Slot - single - background.png')
            img2=Image.open('resource/立绘.png')
            img3=Image.open('resource/Slot - single  精二+黑遮罩.png')
            img4=Image.open('resource/Akteam-rarity_6.png')
            img5=Image.open('resource/潜能5.png')
            img6=Image.open('resource/90.png')
            img7=Image.open('resource/专精3.png')
            img8=Image.open('resource/专精2.png')
            img9=Image.open('resource/专精0.png')




            bg.paste(img1,(startX,startY), mask=img1.split()[3])
            bg.paste(img2,(startX + 12 ,startY + 284 - img2.height), mask=img2)
            bg.paste(img3,(startX + 12 ,startY + 284 - img3.height), mask=img3)
            bg.paste(img4,(startX + 12 ,startY + 284 - img4.height), mask=img4)
            bg.paste(img5,(startX + 16 ,startY + 244), mask=img5)
            bg.paste(img6,(startX + 108 ,startY + 250), mask=img6)
            bg.paste(img7,(startX + 17 ,startY + 292), mask=img7)
            bg.paste(img8,(startX + 62 ,startY + 292), mask=img8)
            bg.paste(img9,(startX + 107 ,startY + 292), mask=img9)

            cnt += 1



            startX += img0.width

        line += 1
        startY += img0.height
    


    bg.show()
    #bg.convert('RGB').save('result.jpg')
    #bg.save('result.png')
    bg.convert('RGB').convert('RGBA').save('result-c.png')
    print('Total Count: ' + str(cnt))

    '''