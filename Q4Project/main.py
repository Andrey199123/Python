import pygame as pg
pg.init()
screen = pg.display.set_mode((1460, 900))
pg.display.set_caption("Q4 Project")
clock = pg.time.Clock()
font = pg.font.Font("Q4Font.otf", 15)
font_title = pg.font.Font("SF Atarian System.ttf", 45)
quiz_font = pg.font.Font("Q4Font.otf", 90)
quiz_title = quiz_font.render("QUIZ", True, "red")
quiz_question = pg.font.Font("SF Atarian System.ttf", 20)
font2 = pg.font.Font("SF Atarian System.ttf", 30)
cannon = pg.image.load("Cannon.png").convert_alpha()
cannon = pg.transform.rotozoom(cannon, 0, 0.2)
back = pg.image.load("BackArrow.png").convert_alpha()
big_back = pg.transform.rotozoom(back, 0, 0.1)
back = pg.transform.rotozoom(back, 0, 0.03)
back2 = pg.transform.flip(back, True, False)
back_rect = back.get_rect(topleft=(0, 5))
back_rect2 = back.get_rect(topleft=(1440, 880))
big_back_rect = big_back.get_rect(topleft=(5, 15))
click = pg.mixer.Sound("ClickSound.mp3")
wrong_sound = pg.mixer.Sound("WrongAnswer.mp3")
right_sound = pg.mixer.Sound("Correct2.wav")
right = pg.image.load("CheckMark.png").convert_alpha()
right = pg.transform.rotozoom(right, 0, 0.07)
wrong = pg.image.load("WrongMark.png").convert_alpha()
wrong = pg.transform.rotozoom(wrong, 0, 0.05)
tokens = 0
tokens_text = font.render("Tokens :", True, (0, 0, 0))
tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
# Madison V Marbury
mvm = pg.image.load("MarburyVMadison.bmp")
mvm_image = pg.image.load("mvm_image.png").convert_alpha()
mvm_image = pg.transform.rotozoom(mvm_image, 0, 0.3)
mvm_image_rect = mvm_image.get_rect(center=(730, 700))
mvm_quiz_image = pg.image.load("MVMQuiz.jpg").convert_alpha()
mvm_quiz_image = pg.transform.rotozoom(mvm_quiz_image, 0, 0.7)
mvm_quiz_image.set_colorkey((0, 0, 0))
mvm_quiz_image_rect = mvm_quiz_image.get_rect(center=(730, 700))
mvm = pg.transform.rotozoom(mvm, 0, 0.82)
mvm_rect = mvm.get_rect(topleft=(15, 40))
mvm_font = font.render("Marbury V Madison", True, "black")
mvm_bool = False
mvm_quiz = False
mvm_quiz1_wrong, mvm_quiz1_right, mvm_quiz2_wrong, mvm_quiz2_right, mvm_quiz3_wrong, mvm_quiz3_right, mvm_quiz4_wrong, mvm_quiz4_right = False, False, False, False, False, False, False, False
mvm1right, mvm1wrong, mvm2right, mvm2wrong, mvm3right, mvm3wrong, mvm4right, mvm4wrong = 0, 0, 0, 0, 0, 0, 0, 0
mvm_title = font_title.render("The US Supreme Court First Declares an Act of Congress Unconstitutional February 24, 1803", True, (234, 234, 234))
mvm_text = font2.render("After John Adams didn't get reelected, he made an effort to pack the political courts with his allies.", True, (234, 234, 234))
mvm_text2 = font2.render("John Marshall, Secretary of State and close advisor of John Adams didn't get to finalize the paperwork", True, (234, 234, 234))
mvm_text3 = font2.render("and deliver the commissions of four of the 42 men Thomas Jefferson elected to serve as justices of the", True, (234, 234, 234))
mvm_text4 = font2.render("peace when he was elected president, one of which was William Marbury. When Jefferson noticed this, he", True, (234, 234, 234))
mvm_text5 = font2.render("told James Madison, his own Secretary of State to hold back the four undelivered commissions. Marbury sued.", True, (234, 234, 234))
mvm_text6 = font2.render("On February 10, 1803, the Supreme Court heard the case. The case depended on three issues. First, did", True, (234, 234, 234))
mvm_text7 = font2.render("and the other appointees have a right to their commissions? Second, if they did have a right that had", True, (234, 234, 234))
mvm_text8 = font2.render("been violated, did federal law provide a remedy? Third, was an order from the U.S. Supreme Court the", True, (234, 234, 234))
mvm_text9 = font2.render("right remedy to solve the problem? The court's decision found that Marbury's and the other appointees'", True, (234, 234, 234))
mvm_text10 = font2.render("rights had been violated by Jefferson when he blocked their commissions. The Supreme Court's ability", True, (234, 234, 234))
mvm_text11 = font2.render("to hear Marbury's case was based on a portion of the judicial act of 1789, which gave the court the", True, (234, 234, 234))
mvm_text12 = font2.render("power to issue writs directly to federal office holders, without a plaintiff having to go through a", True, (234, 234, 234))
mvm_text13 = font2.render("lower court. Marshall proved that this was against Article III, Section 2 of the Constitution, therefore,", True, (234, 234, 234))
mvm_text14 = font2.render("Congress’s enlargement of the Supreme Court’s jurisdiction was unconstitutional. The decision in this", True, (234, 234, 234))
mvm_text15 = font2.render("court case was noticed across America and appeared in many newspapers. Now, the Supreme Court can overrule", True, (234, 234, 234))
mvm_text16 = font2.render("an act of Congress if it is unconstitutional.", True, (234, 234, 234))
# Question 1
mvm_quiz1 = quiz_question.render("How many appointees' commissions were", True, (234, 234, 234))
mvm_quiz1_2 = quiz_question.render("blocked?", True, (234, 234, 234))
mvm_quiz1_text = quiz_question.render("4", True, (234, 234, 234))
mvm_quiz1_text2 = quiz_question.render("5", True, (234, 234, 234))
mvm_quiz1_text3 = quiz_question.render("1", True, (234, 234, 234))
mvm_quiz1_text4 = quiz_question.render("2", True, (234, 234, 234))
mvm_quiz1_text_rect = pg.Rect(583, 215, 5, 5)
mvm_quiz1_text_rect2 = pg.Rect(583, 235, 5, 5)
mvm_quiz1_text_rect3 = pg.Rect(583, 255, 5, 5)
mvm_quiz1_text_rect4 = pg.Rect(583, 275, 5, 5)
# Question 2
mvm_quiz2 = quiz_question.render("Who didn't get to finalize the paperwork", True, (234, 234, 234))
mvm_quiz2_2 = quiz_question.render("and deliver the commissions of four men", True, (234, 234, 234))
mvm_quiz2_3 = quiz_question.render("elected to serve as justices of the peace?", True, (234, 234, 234))
mvm_quiz2_text = quiz_question.render("Thomas Jefferson", True, (234, 234, 234))
mvm_quiz2_text2 = quiz_question.render("John Marshall", True, (234, 234, 234))
mvm_quiz2_text3 = quiz_question.render("John Adams", True, (234, 234, 234))
mvm_quiz2_text4 = quiz_question.render("William Marbury", True, (234, 234, 234))
mvm_quiz2_text_rect = pg.Rect(583, 450, 5, 5)
mvm_quiz2_text_rect2 = pg.Rect(583, 470, 5, 5)
mvm_quiz2_text_rect3 = pg.Rect(583, 490, 5, 5)
mvm_quiz2_text_rect4 = pg.Rect(583, 510, 5, 5)
# Question 3
mvm_quiz3 = quiz_question.render("It is against which section and article for", True, (234, 234, 234))
mvm_quiz3_2 = quiz_question.render("the U.S. Supreme Court to issue writs to", True, (234, 234, 234))
mvm_quiz3_3 = quiz_question.render("issue writs directly to federal office", True, (234, 234, 234))
mvm_quiz3_4 = quiz_question.render("holders, without a plaintiff having to go", True, (234, 234, 234))
mvm_quiz3_5 = quiz_question.render("through a lower court?", True, (234, 234, 234))
mvm_quiz3_text = quiz_question.render("Article 1, Section 8", True, (234, 234, 234))
mvm_quiz3_text2 = quiz_question.render("Article 3, Section 3", True, (234, 234, 234))
mvm_quiz3_text3 = quiz_question.render("Article 3, Section 2", True, (234, 234, 234))
mvm_quiz3_text_rect = pg.Rect(244, 375, 5, 5)
mvm_quiz3_text_rect2 = pg.Rect(244, 395, 5, 5)
mvm_quiz3_text_rect3 = pg.Rect(244, 415, 5, 5)
# Question 4
mvm_quiz4 = quiz_question.render("When did the Supreme Court hear Marbury's", True, (234, 234, 234))
mvm_quiz4_2 = quiz_question.render("case?", True, (234, 234, 234))
mvm_quiz4_text = quiz_question.render("February 24, 1803", True, (234, 234, 234))
mvm_quiz4_text2 = quiz_question.render("February 10, 1803", True, (234, 234, 234))
mvm_quiz4_text3 = quiz_question.render("February 24, 1789", True, (234, 234, 234))
mvm_quiz4_text4 = quiz_question.render("February 10, 1789", True, (234, 234, 234))
mvm_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
mvm_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
mvm_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
mvm_quiz4_text_rect4 = pg.Rect(922, 375, 5, 5)
# Plessy V Ferguson
pvf = pg.image.load("PlessyVFerguson.jpeg")
pvf = pg.transform.rotozoom(pvf, 0, 1.3)
pvf_image = pg.image.load("PVFImage.png").convert_alpha()
pvf_image = pg.transform.rotozoom(pvf_image, 0, 0.3)
pvf_image_rect = pvf_image.get_rect(center=(730, 700))
pvf_quiz_image = pg.image.load("PVFQuiz.jpg").convert_alpha()
pvf_quiz_image.set_colorkey((0, 0, 0))
pvf_quiz_image_rect = pvf_quiz_image.get_rect(center=(730, 700))
pvf_rect = pvf.get_rect(topleft=(430, 40))
pvf_font = font.render("Plessy V Ferguson", True, "black")
pvf_bool = False
pvf_quiz = False
pvf_quiz1_wrong, pvf_quiz1_right, pvf_quiz2_wrong, pvf_quiz2_right, pvf_quiz3_wrong, pvf_quiz3_right, pvf_quiz4_wrong, pvf_quiz4_right = False, False, False, False, False, False, False, False
pvf1right, pvf1wrong, pvf2right, pvf2wrong, pvf3right, pvf3wrong, pvf4right, pvf4wrong = 0, 0, 0, 0, 0, 0, 0, 0
pvf_title = font_title.render("Segregation Becomes Constitutional", True, (234, 234, 234))
pvf_text = font2.render("In 1892, there was an incident in which Homer Plessy refused to sit in a train car for black people because he was 7/8 white and only 1/8 black.", True, (234, 234, 234))
pvf_text2 = font2.render("He was arrested and jailed. He said that his constitutional rights were violated, but the Supreme Court ruled otherwise. He filed a petition", True, (234, 234, 234))
pvf_text3 = font2.render("against the judge, John Ferguson, claiming that the law violated the Equal Protection Clause of the 14th Amendment. On May 18th, 1896, the", True, (234, 234, 234))
pvf_text4 = font2.render("'separate but equal' doctrine according to which laws mandating racial segregation was constitutional as long as the separate facilities of", True, (234, 234, 234))
pvf_text5 = font2.render("each race were equal. So, the Plessy V Ferguson case established that racial segregation was constitutional.", True, (234, 234, 234))
pvf_quiz1 = quiz_question.render("What was Plessy’s white to black ratio?", True, (234, 234, 234))
pvf_quiz2 = quiz_question.render("When did the Supreme Court put up the", True, (234, 234, 234))
pvf_quiz2_2 = quiz_question.render("'separate but equal' doctrine?", True, (234, 234, 234))
pvf_quiz3 = quiz_question.render("How long was segregation constitutional?", True, (234, 234, 234))
pvf_quiz3_2 = quiz_question.render("(Read Brown v Board of education)", True, (234, 234, 234))
pvf_quiz4 = quiz_question.render("Does segregation exist if each race is", True, (234, 234, 234))
pvf_quiz4_2 = quiz_question.render("separated but has equal treatment?", True, (234, 234, 234))
pvf_quiz1_text = quiz_question.render("2 : 1", True, (234, 234, 234))
pvf_quiz1_text2 = quiz_question.render("1 : 2", True, (234, 234, 234))
pvf_quiz1_text3 = quiz_question.render("8 : 1", True, (234, 234, 234))
pvf_quiz1_text4 = quiz_question.render("7 : 1", True, (234, 234, 234))
pvf_quiz2_text = quiz_question.render("1896", True, (234, 234, 234))
pvf_quiz2_text2 = quiz_question.render("1954", True, (234, 234, 234))
pvf_quiz2_text3 = quiz_question.render("1996", True, (234, 234, 234))
pvf_quiz2_text4 = quiz_question.render("1854", True, (234, 234, 234))
pvf_quiz3_text = quiz_question.render("26 years", True, (234, 234, 234))
pvf_quiz3_text2 = quiz_question.render("62 years", True, (234, 234, 234))
pvf_quiz3_text3 = quiz_question.render("58 years", True, (234, 234, 234))
pvf_quiz3_text4 = quiz_question.render("96 years", True, (234, 234, 234))
pvf_quiz4_text = quiz_question.render("Yes", True, (234, 234, 234))
pvf_quiz4_text2 = quiz_question.render("No", True, (234, 234, 234))
pvf_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
pvf_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
pvf_quiz1_text_rect3 = pg.Rect(583, 235, 5, 5)
pvf_quiz1_text_rect4 = pg.Rect(583, 255, 5, 5)
pvf_quiz2_text_rect = pg.Rect(583, 420, 5, 5)
pvf_quiz2_text_rect2 = pg.Rect(583, 440, 5, 5)
pvf_quiz2_text_rect3 = pg.Rect(583, 460, 5, 5)
pvf_quiz2_text_rect4 = pg.Rect(583, 480, 5, 5)
pvf_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
pvf_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
pvf_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
pvf_quiz3_text_rect4 = pg.Rect(244, 375, 5, 5)
pvf_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
pvf_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
# Brown V School Board
bvb = pg.image.load("BrownVBoard.jpeg")
bvb = pg.transform.rotozoom(bvb, 0, 0.3)
bvb_rect = bvb.get_rect(topleft=(678, 40))
bvb_font = font.render("Brown V School Board", True, "black")
bvb_image = pg.image.load("BVBImage.jpg").convert_alpha()
bvb_image = pg.transform.rotozoom(bvb_image, 0, 0.6)
bvb_quiz_image = pg.image.load("BVBQuiz.jpeg").convert_alpha()
bvb_quiz_image = pg.transform.rotozoom(bvb_quiz_image, 0, 0.3)
bvb_quiz_image.set_colorkey((255, 255, 255))
bvb_quiz_image_rect = bvb_quiz_image.get_rect(center=(730, 700))
bvb_image.set_colorkey((0, 0, 0))
bvb_image_rect = bvb_image.get_rect(center=(730, 700))
bvb_bool = False
bvb_quiz = False
bvb_quiz1_wrong, bvb_quiz1_right, bvb_quiz2_wrong, bvb_quiz2_right, bvb_quiz3_wrong, bvb_quiz3_right, bvb_quiz4_wrong, bvb_quiz4_right = False, False, False, False, False, False, False, False
bvb1right, bvb1wrong, bvb2right, bvb2wrong, bvb3right, bvb3wrong, bvb4right, bvb4wrong = 0, 0, 0, 0, 0, 0, 0, 0
bvb_title = font_title.render("The End of Segregation", True, (234, 234, 234))
bvb_text = font2.render("In 1951, Oliver Brown filed a lawsuit against the board of education of Topeka because his daughter was denied to go to Topeka’s all-white", True, (234, 234, 234))
bvb_text2 = font2.render("elementary schools. Brown stated that the schools for blacks weren't equal to the schools for blacks and that it violated the equal protection", True, (234, 234, 234))
bvb_text3 = font2.render("clause, just like Homer Plessy claimed in 1892. The case went to the district court in Kansas in 1951, and it was said that public school", True, (234, 234, 234))
bvb_text4 = font2.render("segregation had a 'detrimental effect upon the colored children', however the “separate but equal” doctrine wasn't removed. Brown’s case and a", True, (234, 234, 234))
bvb_text5 = font2.render("few others related to school segregation made it to the Supreme Court in 1952. The justices were divided on what to do and Chief Justice Fred", True, (234, 234, 234))
bvb_text6 = font2.render("Vinson held the opinion that segregation should still exist. Miraculously, in September of 1953 he died, and was replaced by Earl Warren. After", True, (234, 234, 234))
bvb_text7 = font2.render("this, in 1954, Warren made the decision to end the 'separate but equal' doctrine and said that segregated schools are inherently unequal. As a", True, (234, 234, 234))
bvb_text8 = font2.render("result, the court ruled that segregation was indeed violating the equal protection laws from the 14th Amendment and therefore unconstitutional.", True, (234, 234, 234))
bvb_text9 = font2.render("Also, this ended Jim Crow laws.", True, (234, 234, 234))
bvb_quiz1 = quiz_question.render("When did segregation become constitutional?", True, (234, 234, 234))
bvb_quiz1_2 = quiz_question.render("(Read Plessy V Ferguson)", True, (234, 234, 234))
bvb_quiz2 = quiz_question.render("When was the 'separate but equal' doctrine", True, (234, 234, 234))
bvb_quiz2_2 = quiz_question.render("removed?", True, (234, 234, 234))
bvb_quiz3 = quiz_question.render("Did this case make it to the Supreme Court?", True, (234, 234, 234))
bvb_quiz4 = quiz_question.render("How did segregation end if Chief Justice", True, (234, 234, 234))
bvb_quiz4_2 = quiz_question.render("Fred Vinson was for segregation?", True, (234, 234, 234))
bvb_quiz1_text = quiz_question.render("1900", True, (234, 234, 234))
bvb_quiz1_text2 = quiz_question.render("1960", True, (234, 234, 234))
bvb_quiz1_text3 = quiz_question.render("1854", True, (234, 234, 234))
bvb_quiz1_text4 = quiz_question.render("1896", True, (234, 234, 234))
bvb_quiz2_text = quiz_question.render("1951", True, (234, 234, 234))
bvb_quiz2_text2 = quiz_question.render("1954", True, (234, 234, 234))
bvb_quiz2_text3 = quiz_question.render("1952", True, (234, 234, 234))
bvb_quiz2_text4 = quiz_question.render("1953", True, (234, 234, 234))
bvb_quiz3_text = quiz_question.render("Yes", True, (234, 234, 234))
bvb_quiz3_text2 = quiz_question.render("No", True, (234, 234, 234))
bvb_quiz4_text = quiz_question.render("It didn't.", True, (234, 234, 234))
bvb_quiz4_text2 = quiz_question.render("He was fired.", True, (234, 234, 234))
bvb_quiz4_text3 = quiz_question.render("He died.", True, (234, 234, 234))
bvb_quiz1_text_rect = pg.Rect(583, 215, 5, 5)
bvb_quiz1_text_rect2 = pg.Rect(583, 235, 5, 5)
bvb_quiz1_text_rect3 = pg.Rect(583, 255, 5, 5)
bvb_quiz1_text_rect4 = pg.Rect(583, 275, 5, 5)
bvb_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
bvb_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
bvb_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
bvb_quiz2_text_rect4 = pg.Rect(583, 495, 5, 5)
bvb_quiz3_text_rect = pg.Rect(244, 295, 5, 5)
bvb_quiz3_text_rect2 = pg.Rect(244, 315, 5, 5)
bvb_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
bvb_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
bvb_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
# Gideon V Wainwright
gvw = pg.image.load("GideonVWainwright.jpeg")
gvw = pg.transform.rotozoom(gvw, 0, 1.3)
gvw_image = pg.image.load("GVWImage.jpg").convert_alpha()
gvw_image = pg.transform.rotozoom(gvw_image, 0, 0.6)
gvw_image.set_colorkey((0, 0, 0))
gvw_image_rect = gvw_image.get_rect(center=(730, 700))
gvw_quiz_image = pg.image.load("GVWQuiz.jpg").convert_alpha()
gvw_quiz_image.set_colorkey((0, 0, 0))
gvw_quiz_image_rect = gvw_quiz_image.get_rect(center=(730, 700))
gvw_rect = gvw.get_rect(topleft=(1000, 40))
gvw_font = font.render("Gideon V Wainwright", True, "black")
gvw_bool = False
gvw_quiz = False
gvw_quiz1_wrong, gvw_quiz1_right, gvw_quiz2_wrong, gvw_quiz2_right, gvw_quiz3_wrong, gvw_quiz3_right, gvw_quiz4_wrong, gvw_quiz4_right = False, False, False, False, False, False, False, False
gvw1right, gvw1wrong, gvw2right, gvw2wrong, gvw3right, gvw3wrong, gvw4right, gvw4wrong = 0, 0, 0, 0, 0, 0, 0, 0
gvw_title = font_title.render("Felony Defendants Get a Right to Court-Appointed Attorneys", True, (234, 234, 234))
gvw_text = font2.render("Clearance Gideon was charged in Florida state court with felony breaking and entering. When he went to court without an attorney, he", True, (234, 234, 234))
gvw_text2 = font2.render("requested for the court to appoint one for him. However, an attorney can only be appointed to a defendant in capital cases, so the court", True, (234, 234, 234))
gvw_text3 = font2.render("didn't appoint Gideon an attorney. Gideon represented himself in trial and was found guilty and sentenced to five years in prison. Gideon", True, (234, 234, 234))
gvw_text4 = font2.render("filed a petition in the Florida Supreme Court, arguing that the trial court’s decision violated his constitutional right to be represented", True, (234, 234, 234))
gvw_text5 = font2.render("by counsel. The Florida Supreme Court denied his petition. He then appealed in the Supreme Court of the United States saying that he had", True, (234, 234, 234))
gvw_text6 = font2.render("been denied of his sixth amendment rights. The court agreed to hear the case. The court’s decision was announced as being unanimous in", True, (234, 234, 234))
gvw_text7 = font2.render("favor of Gideon. Now, the 'incorrect trial' rule where the government was given a fair amount of latitude in criminal proceedings as long", True, (234, 234, 234))
gvw_text8 = font2.render("as there were no 'shocking departures from fair procedure', was discarded in favor of a firm set of 'procedural guarantees' based on the", True, (234, 234, 234))
gvw_text9 = font2.render("Constitution. About 2,000 people were freed in Florida alone because of the Gideon decision.", True, (234, 234, 234))
gvw_quiz1 = quiz_question.render("What was Gideon charged with?", True, (234, 234, 234))
gvw_quiz2 = quiz_question.render("How many people were freed from Florida", True, (234, 234, 234))
gvw_quiz2_2 = quiz_question.render("after the Gideon decision?", True, (234, 234, 234))
gvw_quiz3 = quiz_question.render("Which amendment right was Gideon denied", True, (234, 234, 234))
gvw_quiz3_2 = quiz_question.render("from?", True, (234, 234, 234))
gvw_quiz4 = quiz_question.render("For how many years in prison was Gideon", True, (234, 234, 234))
gvw_quiz4_2 = quiz_question.render("sentenced for?", True, (234, 234, 234))
gvw_quiz1_text = quiz_question.render("Perjury", True, (234, 234, 234))
gvw_quiz1_text2 = quiz_question.render("Embezzlement", True, (234, 234, 234))
gvw_quiz1_text3 = quiz_question.render("Conspiracy", True, (234, 234, 234))
gvw_quiz1_text4 = quiz_question.render("Felony", True, (234, 234, 234))
gvw_quiz2_text = quiz_question.render("2,000", True, (234, 234, 234))
gvw_quiz2_text2 = quiz_question.render("5,000", True, (234, 234, 234))
gvw_quiz2_text3 = quiz_question.render("10,000", True, (234, 234, 234))
gvw_quiz2_text4 = quiz_question.render("50,000", True, (234, 234, 234))
gvw_quiz3_text = quiz_question.render("25th Amendment", True, (234, 234, 234))
gvw_quiz3_text2 = quiz_question.render("1st Amendment", True, (234, 234, 234))
gvw_quiz3_text3 = quiz_question.render("6th Amendment", True, (234, 234, 234))
gvw_quiz3_text4 = quiz_question.render("10th Amendment", True, (234, 234, 234))
gvw_quiz4_text = quiz_question.render("10", True, (234, 234, 234))
gvw_quiz4_text2 = quiz_question.render("5", True, (234, 234, 234))
gvw_quiz4_text3 = quiz_question.render("1", True, (234, 234, 234))
gvw_quiz4_text4 = quiz_question.render("0", True, (234, 234, 234))
gvw_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
gvw_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
gvw_quiz1_text_rect3 = pg.Rect(583, 235, 5, 5)
gvw_quiz1_text_rect4 = pg.Rect(583, 255, 5, 5)
gvw_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
gvw_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
gvw_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
gvw_quiz2_text_rect4 = pg.Rect(583, 495, 5, 5)
gvw_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
gvw_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
gvw_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
gvw_quiz3_text_rect4 = pg.Rect(244, 375, 5, 5)
gvw_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
gvw_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
gvw_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
gvw_quiz4_text_rect4 = pg.Rect(922, 375, 5, 5)
# Miranda V Arizona
mva = pg.image.load("MirandaVArizona.jpeg")
mva_image = pg.image.load("MVAImage.jpg").convert_alpha()
mva_image = pg.transform.rotozoom(mva_image, 0, 0.6)
mva_image.set_colorkey((0, 0, 0))
mva_image_rect = mva_image.get_rect(center=(730, 700))
mva_quiz_image = pg.image.load("MVAQuiz.jpg").convert_alpha()
mva_quiz_image = pg.transform.rotozoom(mva_quiz_image, 0, 0.5)
mva_quiz_image.set_colorkey((0, 0, 0))
mva_quiz_image_rect = mva_quiz_image.get_rect(center=(730, 700))
mva_rect = mva.get_rect(topleft=(15, 363))
mva_font = font.render("Miranda V Arizona", True, "black")
mva_bool = False
mva_quiz = False
mva_quiz1_wrong, mva_quiz1_right, mva_quiz2_wrong, mva_quiz2_right, mva_quiz3_wrong, mva_quiz3_right, mva_quiz4_wrong, mva_quiz4_right = False, False, False, False, False, False, False, False
mva1right, mva1wrong, mva2right, mva2wrong, mva3right, mva3wrong, mva4right, mva4wrong = 0, 0, 0, 0, 0, 0, 0, 0
mva_title = font_title.render("Miranda Rights", True, (234, 234, 234))
mva_text = font2.render("Miranda was arrested at his home and taken in custody to a police station where  he was recognized by the witness. Miranda was found", True, (234, 234, 234))
mva_text2 = font2.render("guilty of kidnapping and rape and was sentenced to 20-30 years imprisonment on each count. When Miranda appealed, the Supreme Court", True, (234, 234, 234))
mva_text3 = font2.render("of Arizona stated that his constitutional rights weren't violated. There were three similar cases, in one of which the Supreme Court", True, (234, 234, 234))
mva_text4 = font2.render("of California believed that the defendant should have been advised of his right to remain silent and his right to counsel. The issue", True, (234, 234, 234))
mva_text5 = font2.render("was whether 'procedures which assure that the individual is accorded his privilege under the Fifth Amendment to the Constitution not", True, (234, 234, 234))
mva_text6 = font2.render("to be compelled to incriminate himself' are necessary. In 1966, the Supreme Court stated that a defendant 'must be warned prior to", True, (234, 234, 234))
mva_text7 = font2.render("any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has", True, (234, 234, 234))
mva_text8 = font2.render("the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any", True, (234, 234, 234))
mva_text9 = font2.render("questioning if he so desires.' Now, anytime someone gets arrested, they’re told this, which is called the miranda warning.", True, (234, 234, 234))
mva_quiz1 = quiz_question.render("What is the Miranda warning?", True, (234, 234, 234))
mva_quiz2 = quiz_question.render("How many years was Miranda sentenced", True, (234, 234, 234))
mva_quiz2_2 = quiz_question.render("for?", True, (234, 234, 234))
mva_quiz3 = quiz_question.render("When did the Supreme court decide the", True, (234, 234, 234))
mva_quiz3_2 = quiz_question.render("case?", True, (234, 234, 234))
mva_quiz4 = quiz_question.render("How many similar cases were there?", True, (234, 234, 234))
mva_quiz1_text = quiz_question.render("States your rights after arrest", True, (234, 234, 234))
mva_quiz1_text2 = quiz_question.render("A warning that you are arrested", True, (234, 234, 234))
mva_quiz2_text = quiz_question.render("20-30", True, (234, 234, 234))
mva_quiz2_text2 = quiz_question.render("30-60", True, (234, 234, 234))
mva_quiz2_text3 = quiz_question.render("5-10", True, (234, 234, 234))
mva_quiz3_text = quiz_question.render("1954", True, (234, 234, 234))
mva_quiz3_text2 = quiz_question.render("1896", True, (234, 234, 234))
mva_quiz3_text3 = quiz_question.render("1966", True, (234, 234, 234))
mva_quiz3_text4 = quiz_question.render("1967", True, (234, 234, 234))
mva_quiz4_text = quiz_question.render("0", True, (234, 234, 234))
mva_quiz4_text2 = quiz_question.render("3", True, (234, 234, 234))
mva_quiz4_text3 = quiz_question.render("4", True, (234, 234, 234))
mva_quiz4_text4 = quiz_question.render("2", True, (234, 234, 234))
mva_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
mva_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
mva_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
mva_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
mva_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
mva_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
mva_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
mva_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
mva_quiz3_text_rect4 = pg.Rect(244, 375, 5, 5)
mva_quiz4_text_rect = pg.Rect(922, 295, 5, 5)
mva_quiz4_text_rect2 = pg.Rect(922, 315, 5, 5)
mva_quiz4_text_rect3 = pg.Rect(922, 335, 5, 5)
mva_quiz4_text_rect4 = pg.Rect(922, 355, 5, 5)
# Tinker V Des Moines
tvd = pg.image.load("TinkerVDesMoines.jpeg")
tvd = pg.transform.rotozoom(tvd, 0, 0.3)
tvd_image = pg.image.load("TVDImage.png").convert_alpha()
tvd_image = pg.transform.rotozoom(tvd_image, 0, 0.2)
tvd_image.set_colorkey((0, 0, 0))
tvd_image_rect = tvd_image.get_rect(center=(730, 700))
tvd_quiz_image = pg.image.load("TVDQuiz.jpg").convert_alpha()
tvd_quiz_image = pg.transform.rotozoom(tvd_quiz_image, 0, 0.4)
tvd_quiz_image.set_colorkey((0, 0, 0))
tvd_quiz_image_rect = tvd_quiz_image.get_rect(center=(730, 700))
tvd_rect = tvd.get_rect(topleft=(430, 453))
tvd_font = font.render("Tinker V Des Moines", True, "black")
tvd_bool = False
tvd_quiz = False
tvd_quiz1_wrong, tvd_quiz1_right, tvd_quiz2_wrong, tvd_quiz2_right, tvd_quiz3_wrong, tvd_quiz3_right, tvd_quiz4_wrong, tvd_quiz4_right = False, False, False, False, False, False, False, False
tvd1right, tvd1wrong, tvd2right, tvd2wrong, tvd3right, tvd3wrong, tvd4right, tvd4wrong = 0, 0, 0, 0, 0, 0, 0, 0
tvd_title = font_title.render("Protest Against Vietnam War", True, (234, 234, 234))
tvd_text = font2.render("At a public school in Des Moines, Iowa, Mary Beth Tinker planned to wear black armbands at school as a silent protest against the Vietnam War.", True, (234, 234, 234))
tvd_text2 = font2.render("When the principal found out, he told them that they would be suspended if they kept wearing them to school, since they will cause a", True, (234, 234, 234))
tvd_text3 = font2.render("disruption to the learning environment. Despite the warning, some students wore the armbands and were suspended. During their suspension, the", True, (234, 234, 234))
tvd_text4 = font2.render("students' parents sued the school for violating their children's right to free speech. he question posed by the case was whether the symbolic", True, (234, 234, 234))
tvd_text5 = font2.render("speech of students in public schools should be protected by the First Amendment. The U.S. District Court for the Southern District of Iowa sided", True, (234, 234, 234))
tvd_text6 = font2.render("with the school’s position, ruling that wearing the armbands could disrupt learning. The students appealed the ruling to the U.S. Court of Appeals", True, (234, 234, 234))
tvd_text7 = font2.render("but lost and took the case to the Supreme Court of the United States. In 1969, in a 7-2 decision, the Supreme Court’s majority ruled that neither", True, (234, 234, 234))
tvd_text8 = font2.render("students nor teachers 'shed their constitutional rights to freedom of speech or expression at the schoolhouse gate.' So, The court found that the", True, (234, 234, 234))
tvd_text9 = font2.render("First Amendment applied to public schools and school officials couldn't stop students from expressing themselves unless it disrupted the", True, (234, 234, 234))
tvd_text10 = font2.render("educational process.", True, (234, 234, 234))
tvd_quiz1 = quiz_question.render("Did the students win the appeal?", True, (234, 234, 234))
tvd_quiz2 = quiz_question.render("What was the vote in favor of Tinker?", True, (234, 234, 234))
tvd_quiz3 = quiz_question.render("Which amendment did this case have to do", True, (234, 234, 234))
tvd_quiz3_2 = quiz_question.render("with?", True, (234, 234, 234))
tvd_quiz4 = quiz_question.render("Did the U.S. District Court for the", True, (234, 234, 234))
tvd_quiz4_2 = quiz_question.render("Southern District of Iowa side with", True, (234, 234, 234))
tvd_quiz4_3 = quiz_question.render("the school?", True, (234, 234, 234))
tvd_quiz1_text = quiz_question.render("Yes", True, (234, 234, 234))
tvd_quiz1_text2 = quiz_question.render("No", True, (234, 234, 234))
tvd_quiz2_text = quiz_question.render("9-0", True, (234, 234, 234))
tvd_quiz2_text2 = quiz_question.render("8-1", True, (234, 234, 234))
tvd_quiz2_text3 = quiz_question.render("7-2", True, (234, 234, 234))
tvd_quiz2_text4 = quiz_question.render("5-4", True, (234, 234, 234))
tvd_quiz3_text = quiz_question.render("3", True, (234, 234, 234))
tvd_quiz3_text2 = quiz_question.render("5", True, (234, 234, 234))
tvd_quiz3_text3 = quiz_question.render("10", True, (234, 234, 234))
tvd_quiz3_text4 = quiz_question.render("1", True, (234, 234, 234))
tvd_quiz4_text = quiz_question.render("Yes", True, (234, 234, 234))
tvd_quiz4_text2 = quiz_question.render("No", True, (234, 234, 234))
tvd_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
tvd_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
tvd_quiz2_text_rect = pg.Rect(583, 415, 5, 5)
tvd_quiz2_text_rect2 = pg.Rect(583, 435, 5, 5)
tvd_quiz2_text_rect3 = pg.Rect(583, 455, 5, 5)
tvd_quiz2_text_rect4 = pg.Rect(583, 475, 5, 5)
tvd_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
tvd_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
tvd_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
tvd_quiz3_text_rect4 = pg.Rect(244, 375, 5, 5)
tvd_quiz4_text_rect = pg.Rect(922, 335, 5, 5)
tvd_quiz4_text_rect2 = pg.Rect(922, 355, 5, 5)
# In Re Gault
irg = pg.image.load("InReGault.jpeg")
irg = pg.transform.rotozoom(irg, 0, 1.3)
irg_image = pg.image.load("IRGImage.png").convert_alpha()
irg_image = pg.transform.rotozoom(irg_image, 0, 0.9)
irg_image_rect = irg_image.get_rect(center=(730, 700))
irg_quiz_image = pg.image.load("IRGQuiz.png").convert_alpha()
irg_quiz_image = pg.transform.rotozoom(irg_quiz_image, 0, 0.5)
irg_quiz_image_rect = irg_quiz_image.get_rect(center=(730, 700))
irg_rect = irg.get_rect(topleft=(805, 479))
irg_font = font.render("In Re Gault", True, "black")
irg_bool = False
irg_quiz = False
irg_quiz1_wrong, irg_quiz1_right, irg_quiz2_wrong, irg_quiz2_right, irg_quiz3_wrong, irg_quiz3_right, irg_quiz4_wrong, irg_quiz4_right = False, False, False, False, False, False, False, False
irg1right, irg1wrong, irg2right, irg2wrong, irg3right, irg3wrong, irg4right, irg4wrong = 0, 0, 0, 0, 0, 0, 0, 0
irg_title = font_title.render("Juvenile Rights", True, (234, 234, 234))
irg_text = font2.render("Gerald Gault, at 15 year old at the time was accused of making an obscene telephone call to to a neighbor, Mrs. Cook, on June 8, 1964. The police", True, (234, 234, 234))
irg_text2 = font2.render("did not leave notice with Gault's parents, who were at work, when he was arrested. There was a hearing, and at the end of it, the judge committed", True, (234, 234, 234))
irg_text3 = font2.render("Gault to juvenile detention for six years, until he turned 21. Some of the hearings were informal. Not only was Mrs. Cook not present, but no", True, (234, 234, 234))
irg_text4 = font2.render("transcript nor recording was made, and no one was sworn in prior to testifying. The question was whether the procedures used to commit Gault", True, (234, 234, 234))
irg_text5 = font2.render("constitutionally legitimate under the Due Process Clause of the Fourteenth Amendment were right to do. Gault's parents filed a petition for a writ", True, (234, 234, 234))
irg_text6 = font2.render("habeus corpus which was dismissed by both the Superior Court of Arizona and the Arizona Supreme Court. The Gault's next sought relief in the", True, (234, 234, 234))
irg_text7 = font2.render("Supreme Court of the United States. The Court agreed to hear the case to determine the procedural due process rights of a juvenile criminal", True, (234, 234, 234))
irg_text8 = font2.render("defendant. There was an 8-1 decision for Gault, meaning that the proceedings of the Juvenile Court were unconstitutional, because there was no", True, (234, 234, 234))
irg_text9 = font2.render("adequate notice of charges, notification of both parents’ and the child’s right to counsel, opportunity for confrontation and cross-examination at", True, (234, 234, 234))
irg_text10 = font2.render("the hearings, and adequate safeguards against self-incrimination. Gerald’s sixth amendment had been violated. This was the first time where the", True, (234, 234, 234))
irg_text11 = font2.render("Supreme Court held that children have many of the same legal rights as adults in criminal court, including the right to an attorney, the right to", True, (234, 234, 234))
irg_text12 = font2.render("remain silent, the right to notice of the charges, and the right to a full hearing on the merits of the case.", True, (234, 234, 234))
irg_quiz1 = quiz_question.render("Which amendment violated in hearings?", True, (234, 234, 234))
irg_quiz2 = quiz_question.render("How old was Gerald Gault when he was", True, (234, 234, 234))
irg_quiz2_2 = quiz_question.render("accused?", True, (234, 234, 234))
irg_quiz3 = quiz_question.render("For how many years was Gerald Gault", True, (234, 234, 234))
irg_quiz3_2 = quiz_question.render("sentenced for juvenile detention?", True, (234, 234, 234))
irg_quiz4 = quiz_question.render("Which was constitutional in the", True, (234, 234, 234))
irg_quiz4_2 = quiz_question.render("proceedings of the Juvenile Court?", True, (234, 234, 234))
irg_quiz1_text = quiz_question.render("6", True, (234, 234, 234))
irg_quiz1_text2 = quiz_question.render("10", True, (234, 234, 234))
irg_quiz1_text3 = quiz_question.render("1", True, (234, 234, 234))
irg_quiz1_text4 = quiz_question.render("2", True, (234, 234, 234))
irg_quiz2_text = quiz_question.render("18", True, (234, 234, 234))
irg_quiz2_text2 = quiz_question.render("17", True, (234, 234, 234))
irg_quiz2_text3 = quiz_question.render("15", True, (234, 234, 234))
irg_quiz2_text4 = quiz_question.render("12", True, (234, 234, 234))
irg_quiz3_text = quiz_question.render("1", True, (234, 234, 234))
irg_quiz3_text2 = quiz_question.render("0", True, (234, 234, 234))
irg_quiz3_text3 = quiz_question.render("5", True, (234, 234, 234))
irg_quiz3_text4 = quiz_question.render("6", True, (234, 234, 234))
irg_quiz4_text = quiz_question.render("No adequate notice of charges", True, (234, 234, 234))
irg_quiz4_text2 = quiz_question.render("No safe-guards against incrimination", True, (234, 234, 234))
irg_quiz4_text3 = quiz_question.render("Not being told right to remain silent", True, (234, 234, 234))
irg_quiz4_text4 = quiz_question.render("No notification of right to counsel", True, (234, 234, 234))
irg_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
irg_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
irg_quiz1_text_rect3 = pg.Rect(583, 235, 5, 5)
irg_quiz1_text_rect4 = pg.Rect(583, 255, 5, 5)
irg_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
irg_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
irg_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
irg_quiz2_text_rect4 = pg.Rect(583, 495, 5, 5)
irg_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
irg_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
irg_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
irg_quiz3_text_rect4 = pg.Rect(244, 375, 5, 5)
irg_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
irg_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
irg_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
irg_quiz4_text_rect4 = pg.Rect(922, 375, 5, 5)
# Hazelwood V Kuhlmeier
hvk = pg.image.load("HazelwoodVKuhlmeier.png")
hvk = pg.transform.rotozoom(hvk, 0, 0.6)
hvk_image = pg.image.load("HVKImage.png").convert_alpha()
hvk_image = pg.transform.rotozoom(hvk_image, 0, 0.9)
hvk_image_rect = hvk_image.get_rect(center=(730, 700))
hvk_quiz_image = pg.image.load("HVKQuiz.png").convert_alpha()
hvk_quiz_image = pg.transform.rotozoom(hvk_quiz_image, 0, 0.3)
hvk_quiz_image_rect = hvk_quiz_image.get_rect(center=(730, 700))
hvk_rect = hvk.get_rect(topleft=(430, 692))
hvk_font = font.render("Hazelwood V Kuhlmeier", True, "black")
hvk_bool = False
hvk_quiz = False
hvk_quiz1_wrong, hvk_quiz1_right, hvk_quiz2_wrong, hvk_quiz2_right, hvk_quiz3_wrong, hvk_quiz3_right, hvk_quiz4_wrong, hvk_quiz4_right = False, False, False, False, False, False, False, False
hvk1right, hvk1wrong, hvk2right, hvk2wrong = 0, 0, 0, 0
hvk_title = font_title.render("Public School Newspaper", True, (234, 234, 234))
hvk_text = font2.render("In 1983, at Hazelwood East High School in St. Louis, Missouri, students wrote stories about their peers’ experiences with teen pregnancy and the", True, (234, 234, 234))
hvk_text2 = font2.render("impact of divorce. When they published the articles in the school-sponsored newspaper, the principal deleted the pages that contained the stories", True, (234, 234, 234))
hvk_text3 = font2.render("prior to publication without telling the students. The students believed that the school violated their first amendment rights, and took their case", True, (234, 234, 234))
hvk_text4 = font2.render("to the U.S District Court for the Eastern District of Missouri in St.Louis. The trial court ruled that the school had the authority to remove", True, (234, 234, 234))
hvk_text5 = font2.render("articles that were written as part of a class. The students appealed to the U.S. Court of Appeals, and it was found that the newspaper was a", True, (234, 234, 234))
hvk_text6 = font2.render("public forum that extended beyond the walls of the school. It decided that school officials could censor the content only under extreme", True, (234, 234, 234))
hvk_text7 = font2.render("circumstances. The school applied to the Supreme Court of the U.S. In a 5-3 decision, the Supreme Court stated that the principals actions didn't", True, (234, 234, 234))
hvk_text8 = font2.render("violate the first amendment, since the paper was sponsored by the school.", True, (234, 234, 234))
hvk_quiz1 = quiz_question.render("Why didn't the principals actions", True, (234, 234, 234))
hvk_quiz1_2 = quiz_question.render("violate the first amendment?", True, (234, 234, 234))
hvk_quiz2 = quiz_question.render("Why did the principal delete the", True, (234, 234, 234))
hvk_quiz2_2 = quiz_question.render("pages?", True, (234, 234, 234))
hvk_quiz1_text = quiz_question.render("The paper was sponsored by the school", True, (234, 234, 234))
hvk_quiz1_text2 = quiz_question.render("The paper had inappropriate content", True, (234, 234, 234))
hvk_quiz2_text = quiz_question.render("He found them inappropriate", True, (234, 234, 234))
hvk_quiz2_text2 = quiz_question.render("The pages weren't school-related.", True, (234, 234, 234))
hvk_quiz1_text_rect = pg.Rect(583, 215, 5, 5)
hvk_quiz1_text_rect2 = pg.Rect(583, 235, 5, 5)
hvk_quiz2_text_rect = pg.Rect(583, 430, 5, 5)
hvk_quiz2_text_rect2 = pg.Rect(583, 450, 5, 5)
# US V Nixon
usvn = pg.image.load("USVNixon.jpeg")
usvn = pg.transform.rotozoom(usvn, 0, 1.3)
usvn_image = pg.image.load("USVNImage.png").convert_alpha()
usvn_image = pg.transform.rotozoom(usvn_image, 0, 1.3)
usvn_image_rect = usvn_image.get_rect(center=(730, 700))
usvn_quiz_image = pg.image.load("USVNQuiz.png").convert_alpha()
usvn_quiz_image = pg.transform.rotozoom(usvn_quiz_image, 0, 0.4)
usvn_quiz_image_rect = usvn_quiz_image.get_rect(center=(730, 700))
usvn_rect = usvn.get_rect(topleft=(1146, 479))
usvn_font = font.render("US V Nixon", True, "black")
usvn_bool = False
usvn_quiz = False
usvn_title = font_title.render("Nixon Backs Down", True, (234, 234, 234))
usvn_quiz1_wrong, usvn_quiz1_right, usvn_quiz2_wrong, usvn_quiz2_right, usvn_quiz3_wrong, usvn_quiz3_right, usvn_quiz4_wrong, usvn_quiz4_right = False, False, False, False, False, False, False, False
usvn1right, usvn1wrong, usvn2right, usvn2wrong, usvn3right, usvn3wrong, usvn4right, usvn4wrong = 0, 0, 0, 0, 0, 0, 0, 0
usvn_text = font2.render("During the 1972 presidential campaign between Nixon and George McGovern, five months before the election, five men broke into Democratic", True, (234, 234, 234))
usvn_text2 = font2.render("National Committee headquarters to spy on the Democratic party. These men were found to have ties with Nixon. In 1974, special prosecutor", True, (234, 234, 234))
usvn_text3 = font2.render("Jaworski obtained a subpoena ordering Nixon to release certain tapes and papers related to specific meeting between Nixon and those indicted", True, (234, 234, 234))
usvn_text4 = font2.render("by the grand jury, and some of those tapes talked about the planned break-in. As the Supreme Court drama was unfolding, the House Judiciary", True, (234, 234, 234))
usvn_text5 = font2.render("Committee worked on three articles of impeachment against President Nixon. The evidence on the tapes was critical to the impending House", True, (234, 234, 234))
usvn_text6 = font2.render("impeachment proceedings against Nixon. The Court ordered the tapes released as soon as possible after a judge had listened to the tapes to", True, (234, 234, 234))
usvn_text7 = font2.render("decide they were relevant to the trial of the former Nixon aides. On July 24, 1974, a unanimous Court ruled against the President. About two", True, (234, 234, 234))
usvn_text8 = font2.render("weeks after the Supreme Court’s decision, Nixon resigned from office. United States v. Nixon is considered a crucial precedent limiting the", True, (234, 234, 234))
usvn_text9 = font2.render("power of any U.S. president to claim executive privilege.", True, (234, 234, 234))
usvn_quiz1 = quiz_question.render("Which party was Nixon for?", True, (234, 234, 234))
usvn_quiz2 = quiz_question.render("How many articles of impeachment were", True, (234, 234, 234))
usvn_quiz2_2 = quiz_question.render("there against Nixon?", True, (234, 234, 234))
usvn_quiz3 = quiz_question.render("Why did Nixon break into the Democratic", True, (234, 234, 234))
usvn_quiz3_2 = quiz_question.render("National Committee?", True, (234, 234, 234))
usvn_quiz4 = quiz_question.render("After how much time did Nixon resign", True, (234, 234, 234))
usvn_quiz4_2 = quiz_question.render("after the Supreme Court decision?", True, (234, 234, 234))
usvn_quiz1_text = quiz_question.render("Republican", True, (234, 234, 234))
usvn_quiz1_text2 = quiz_question.render("Democratic", True, (234, 234, 234))
usvn_quiz2_text = quiz_question.render("3", True, (234, 234, 234))
usvn_quiz2_text2 = quiz_question.render("5", True, (234, 234, 234))
usvn_quiz2_text3 = quiz_question.render("1", True, (234, 234, 234))
usvn_quiz2_text4 = quiz_question.render("2", True, (234, 234, 234))
usvn_quiz3_text = quiz_question.render("To spy on the Democratic party.", True, (234, 234, 234))
usvn_quiz3_text2 = quiz_question.render("To destroy important information.", True, (234, 234, 234))
usvn_quiz3_text3 = quiz_question.render("Nixon had no control over this.", True, (234, 234, 234))
usvn_quiz4_text = quiz_question.render("On the same day", True, (234, 234, 234))
usvn_quiz4_text2 = quiz_question.render("A few days", True, (234, 234, 234))
usvn_quiz4_text3 = quiz_question.render("1 month", True, (234, 234, 234))
usvn_quiz4_text4 = quiz_question.render("2 weeks", True, (234, 234, 234))
usvn_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
usvn_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
usvn_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
usvn_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
usvn_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
usvn_quiz2_text_rect4 = pg.Rect(583, 495, 5, 5)
usvn_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
usvn_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
usvn_quiz3_text_rect3 = pg.Rect(244, 355, 5, 5)
usvn_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
usvn_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
usvn_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
usvn_quiz4_text_rect4 = pg.Rect(922, 375, 5, 5)
# Bush V Gore
bvg = pg.image.load("BushVGore.jpeg")
bvg = pg.transform.rotozoom(bvg, 0, 0.13)
bvg_image = pg.image.load("BVGImage.png").convert_alpha()
bvg_image_rect = bvg_image.get_rect(center=(730, 750))
bvg_quiz_image = pg.image.load("BVGQuiz.png").convert_alpha()
bvg_quiz_image_rect = bvg_quiz_image.get_rect(center=(730, 700))
bvg_rect = bvg.get_rect(topleft=(678, 308))
bvg_font = font.render("Bush V Gore", True, "black")
bvg_bool = False
bvg_quiz = False
bvg_quiz1_wrong, bvg_quiz1_right, bvg_quiz2_wrong, bvg_quiz2_right, bvg_quiz3_wrong, bvg_quiz3_right, bvg_quiz4_wrong, bvg_quiz4_right = False, False, False, False, False, False, False, False
bvg1right, bvg1wrong, bvg2right, bvg2wrong, bvg3right, bvg3wrong, bvg4right, bvg4wrong = 0, 0, 0, 0, 0, 0, 0, 0
bvg_title = font_title.render("Closest election ever in the United States", True, (234, 234, 234))
bvg_text = font2.render("The 2000 election was very close between Bush and Gore. The contest focused on Florida, and fewer than 600 votes separated the candidates", True, (234, 234, 234))
bvg_text2 = font2.render("there. At about 3:00 AM Gore called a stunned Bush to retract his concession. In Florida, if the margin of victory between both candidates", True, (234, 234, 234))
bvg_text3 = font2.render("is less than 0.5 percent, a vote recount is needed. In this case, the gap was 0.01 percent. After the recount, Bush led by 327 votes out of", True, (234, 234, 234))
bvg_text4 = font2.render("6 million. In the month following the election, some 50 individual suits were filed concerning the various counts, recounts, and", True, (234, 234, 234))
bvg_text5 = font2.render("certification deadlines. On December 8, in a 4-3 decision, the Florida Supreme Court ordered immediate manual recounts of undervotes for the", True, (234, 234, 234))
bvg_text6 = font2.render("office of president in all counties where such recounts had not already taken place by November 14th. 3 out of 4 of those counties were", True, (234, 234, 234))
bvg_text7 = font2.render("unable to do this by the deadline. Then, late returns were accepted only if their tardiness was justified by each county in writing by 2 p.m.", True, (234, 234, 234))
bvg_text8 = font2.render("November 15th. The three counties sent an explanation for the delay, but Secretary Harris rejected their explanations and announced that the", True, (234, 234, 234))
bvg_text9 = font2.render("final Florida vote count would be announces Saturday, November 18th, 2000. The tables turned again after Vice President Gore and Palm Beach", True, (234, 234, 234))
bvg_text10 = font2.render("County filed an injunction against Secretary Harris to prevent her from certifying the election until the three counties could finish their", True, (234, 234, 234))
bvg_text11 = font2.render("recounts. The Supreme Court issued the injunction on November 17. Meanwhile, Miami-Dade stopped manually counting ballots allegedly certain", True, (234, 234, 234))
bvg_text12 = font2.render("that it could not complete its recount by the November 26 deadline. Gore sought but failed to obtain a court order for Miami-Dade to", True, (234, 234, 234))
bvg_text13 = font2.render("continue counting. On November 26, with, at this point, just 537 votes separating Bush and Gore, Secretary Harris certified the election for", True, (234, 234, 234))
bvg_text14 = font2.render("Bush. The next day, Gore sued the secretary, alleging that the certified results were illegitimate because the recount process was not yet ", True, (234, 234, 234))
bvg_text15 = font2.render("complete. After a local court dismissed the suit, Gore appealed to the Florida Supreme Court, which ruled on December 8 that all Florida", True, (234, 234, 234))
bvg_text16 = font2.render("ballots cast but not counted by voting machines must be manually recounted if they had not been already. In many counties, machines did not", True, (234, 234, 234))
bvg_text17 = font2.render("register votes because of defects in punch-card ballots. Governor Bush appealed this decision to the U.S. Supreme Court, which expeditiously", True, (234, 234, 234))
bvg_text18 = font2.render("reviewed the case on December 9. The Supreme Court found that because of inconsistencies in recounting between Florida counties, the Florida ", True, (234, 234, 234))
bvg_text19 = font2.render("court’s order of a manual recount amounted to a violation of the equal protection clause of the Fourteenth Amendment. The Court also ruled", True, (234, 234, 234))
bvg_text20 = font2.render("that no new recount should take place.", True, (234, 234, 234))
bvg_quiz1 = quiz_question.render("What are undervotes?", True, (234, 234, 234))
bvg_quiz2 = quiz_question.render("How many counties couldn't finish", True, (234, 234, 234))
bvg_quiz2_2 = quiz_question.render("counting the votes?", True, (234, 234, 234))
bvg_quiz3 = quiz_question.render("Were the late returns from the", True, (234, 234, 234))
bvg_quiz3_2 = quiz_question.render("counties accepted?", True, (234, 234, 234))
bvg_quiz4 = quiz_question.render("What was the gap between Bush", True, (234, 234, 234))
bvg_quiz4_2 = quiz_question.render("and Gore?", True, (234, 234, 234))
bvg_quiz1_text = quiz_question.render("Cast Ballots but not counted", True, (234, 234, 234))
bvg_quiz1_text2 = quiz_question.render("A vote going to other party", True, (234, 234, 234))
bvg_quiz1_text3 = quiz_question.render("A vote counting as negative", True, (234, 234, 234))
bvg_quiz1_text4 = quiz_question.render("A vote counted as two", True, (234, 234, 234))
bvg_quiz2_text = quiz_question.render("1", True, (234, 234, 234))
bvg_quiz2_text2 = quiz_question.render("2", True, (234, 234, 234))
bvg_quiz2_text3 = quiz_question.render("3", True, (234, 234, 234))
bvg_quiz2_text4 = quiz_question.render("4", True, (234, 234, 234))
bvg_quiz3_text = quiz_question.render("Yes", True, (234, 234, 234))
bvg_quiz3_text2 = quiz_question.render("No", True, (234, 234, 234))
bvg_quiz4_text = quiz_question.render("0.01 percent", True, (234, 234, 234))
bvg_quiz4_text2 = quiz_question.render("0.5 percent", True, (234, 234, 234))
bvg_quiz4_text3 = quiz_question.render("1 percent", True, (234, 234, 234))
bvg_quiz4_text4 = quiz_question.render("5 percent", True, (234, 234, 234))
bvg_quiz1_text_rect = pg.Rect(583, 195, 5, 5)
bvg_quiz1_text_rect2 = pg.Rect(583, 215, 5, 5)
bvg_quiz1_text_rect3 = pg.Rect(583, 235, 5, 5)
bvg_quiz1_text_rect4 = pg.Rect(583, 255, 5, 5)
bvg_quiz2_text_rect = pg.Rect(583, 435, 5, 5)
bvg_quiz2_text_rect2 = pg.Rect(583, 455, 5, 5)
bvg_quiz2_text_rect3 = pg.Rect(583, 475, 5, 5)
bvg_quiz2_text_rect4 = pg.Rect(583, 495, 5, 5)
bvg_quiz3_text_rect = pg.Rect(244, 315, 5, 5)
bvg_quiz3_text_rect2 = pg.Rect(244, 335, 5, 5)
bvg_quiz4_text_rect = pg.Rect(922, 315, 5, 5)
bvg_quiz4_text_rect2 = pg.Rect(922, 335, 5, 5)
bvg_quiz4_text_rect3 = pg.Rect(922, 355, 5, 5)
bvg_quiz4_text_rect4 = pg.Rect(922, 375, 5, 5)
play = False
check_bool = False
print(len([name for name in globals()]), "variables")
while True:
    time = pg.time.get_ticks()
    mouse = pg.mouse.get_pos()
    screen.fill((64, 64, 64))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    if mvm_bool == False and mvm_quiz == False and pvf_bool == False and pvf_quiz == False and bvb_bool == False and bvb_quiz == False and gvw_bool == False and gvw_quiz == False and mva_bool == False and mva_quiz == False and tvd_bool == False and tvd_quiz == False and irg_bool == False and irg_quiz == False and hvk_bool == False and hvk_quiz == False and usvn_bool == False and usvn_quiz == False and bvg_bool == False and bvg_quiz == False:
        # Tokens
        pg.draw.rect(screen, (227, 207, 87), (15, 688, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 688))
        screen.blit(tokens_text2, (100, 688))
        # Marbury V Madison
        pg.draw.rect(screen, (234, 234, 234), (15, 15, 409, 308), border_radius=10)
        screen.blit(mvm, mvm_rect)
        screen.blit(mvm_font, (30, 20))
        # Plessy V Ferguson
        pg.draw.rect(screen, (234, 234, 234), (430, 15, 233, 398), border_radius=10)
        screen.blit(pvf, pvf_rect)
        screen.blit(pvf_font, (445, 20))
        # Brown V School Board
        pg.draw.rect(screen, (234, 234, 234), (678, 15, 307, 265), border_radius=10)
        screen.blit(bvb, bvb_rect)
        screen.blit(bvb_font, (693, 20))
        # Gideon V Wainwright
        pg.draw.rect(screen, (234, 234, 234), (1000, 15, 271, 424), border_radius=10)
        screen.blit(gvw, gvw_rect)
        screen.blit(gvw_font, (1015, 20))
        # Miranda v Arizona
        pg.draw.rect(screen, (234, 234, 234), (15, 338, 400, 335), border_radius=10)
        screen.blit(mva, mva_rect)
        screen.blit(mva_font, (30, 343))
        # Tinker V Des Moines
        pg.draw.rect(screen, (234, 234, 234), (430, 428, 360, 224), border_radius=10)
        screen.blit(tvd, tvd_rect)
        screen.blit(tvd_font, (445, 433))
        # In Re Gault
        pg.draw.rect(screen, (234, 234, 234), (805, 454, 326, 296), border_radius=10)
        screen.blit(irg, irg_rect)
        screen.blit(irg_font, (820, 459))
        # Hazelwood V Kuhlmeier
        pg.draw.rect(screen, (234, 234, 234), (430, 667, 332, 216), border_radius=10)
        screen.blit(hvk, hvk_rect)
        screen.blit(hvk_font, (445, 672))
        # US V Nixon
        pg.draw.rect(screen, (234, 234, 234), (1146, 454, 239, 391), border_radius=10)
        screen.blit(usvn, usvn_rect)
        screen.blit(usvn_font, (1161, 459))
        # Bush V Gore
        pg.draw.rect(screen, (234, 234, 234), (678, 295, 207, 121), border_radius=10)
        screen.blit(bvg, bvg_rect)
        screen.blit(bvg_font, (693, 293))
    if not check_bool:
        if mvm_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_bool = True
            click.play(0)
        if pvf_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_bool = True
            click.play(0)
        elif bvb_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_bool = True
            click.play(0)
        elif gvw_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_bool = True
            click.play(0)
        elif mva_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_bool = True
            click.play(0)
        elif tvd_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_bool = True
            click.play(0)
        elif irg_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_bool = True
            click.play(0)
        elif hvk_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_bool = True
            click.play(0)
        elif usvn_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_bool = True
            click.play(0)
        elif bvg_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_bool = True
            click.play(0)
    if mvm_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_bool = False
            mvm_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(mvm_title, (10, 30))
        screen.blit(mvm_text, (10, 75))
        screen.blit(mvm_text2, (10, 105))
        screen.blit(mvm_text3, (10, 135))
        screen.blit(mvm_text4, (10, 165))
        screen.blit(mvm_text5, (10, 195))
        screen.blit(mvm_text6, (10, 225))
        screen.blit(mvm_text7, (10, 255))
        screen.blit(mvm_text8, (10, 285))
        screen.blit(mvm_text9, (10, 315))
        screen.blit(mvm_text10, (10, 345))
        screen.blit(mvm_text11, (10, 375))
        screen.blit(mvm_text12, (10, 405))
        screen.blit(mvm_text13, (10, 435))
        screen.blit(mvm_text14, (10, 465))
        screen.blit(mvm_text15, (10, 495))
        screen.blit(mvm_text16, (10, 525))
        screen.blit(mvm_image, mvm_image_rect)
        pg.draw.rect(screen, (152, 245, 255), (550, 580, 360, 240), width=5, border_radius=25)
    elif pvf_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_bool = False
            pvf_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(pvf_title, (10, 30))
        screen.blit(pvf_text, (10, 75))
        screen.blit(pvf_text2, (10, 105))
        screen.blit(pvf_text3, (10, 135))
        screen.blit(pvf_text4, (10, 165))
        screen.blit(pvf_text5, (10, 195))
        screen.blit(pvf_image, pvf_image_rect)
        pg.draw.rect(screen, (152, 245, 255), pvf_image_rect, width=5, border_radius=35)
    elif bvb_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_bool = False
            bvb_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(bvb_image, bvb_image_rect)
        pg.draw.rect(screen, (152, 245, 255), bvb_image_rect, width=5, border_radius=25)
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(bvb_title, (10, 30))
        screen.blit(bvb_text, (10, 75))
        screen.blit(bvb_text2, (10, 105))
        screen.blit(bvb_text3, (10, 135))
        screen.blit(bvb_text4, (10, 165))
        screen.blit(bvb_text5, (10, 195))
        screen.blit(bvb_text6, (10, 225))
        screen.blit(bvb_text7, (10, 255))
        screen.blit(bvb_text8, (10, 285))
    elif gvw_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_bool = False
            gvw_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(gvw_image, gvw_image_rect)
        pg.draw.rect(screen, (152, 245, 255), gvw_image_rect, width=5, border_radius=25)
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(gvw_title, (10, 30))
        screen.blit(gvw_text, (10, 75))
        screen.blit(gvw_text2, (10, 105))
        screen.blit(gvw_text3, (10, 135))
        screen.blit(gvw_text4, (10, 165))
        screen.blit(gvw_text5, (10, 195))
        screen.blit(gvw_text6, (10, 225))
        screen.blit(gvw_text7, (10, 255))
        screen.blit(gvw_text8, (10, 285))
        screen.blit(gvw_text9, (10, 315))
    elif mva_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_bool = False
            mva_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(mva_image, mva_image_rect)
        pg.draw.rect(screen, (152, 245, 255), mva_image_rect, width=5, border_radius=25)
        screen.blit(mva_title, (10, 30))
        screen.blit(mva_text, (10, 75))
        screen.blit(mva_text2, (10, 105))
        screen.blit(mva_text3, (10, 135))
        screen.blit(mva_text4, (10, 165))
        screen.blit(mva_text5, (10, 195))
        screen.blit(mva_text6, (10, 225))
        screen.blit(mva_text7, (10, 255))
        screen.blit(mva_text8, (10, 285))
        screen.blit(mva_text9, (10, 315))
    elif tvd_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_bool = False
            tvd_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(tvd_image, tvd_image_rect)
        pg.draw.rect(screen, (152, 245, 255), tvd_image_rect, width=5, border_radius=20)
        screen.blit(tvd_title, (10, 30))
        screen.blit(tvd_text, (10, 75))
        screen.blit(tvd_text2, (10, 105))
        screen.blit(tvd_text3, (10, 135))
        screen.blit(tvd_text4, (10, 165))
        screen.blit(tvd_text5, (10, 195))
        screen.blit(tvd_text6, (10, 225))
        screen.blit(tvd_text7, (10, 255))
        screen.blit(tvd_text8, (10, 285))
        screen.blit(tvd_text9, (10, 315))
        screen.blit(tvd_text10, (10, 345))
    elif irg_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_bool = False
            irg_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(irg_image, irg_image_rect)
        pg.draw.rect(screen, (152, 245, 255), irg_image_rect, width=5, border_radius=20)
        screen.blit(irg_title, (10, 30))
        screen.blit(irg_text, (10, 75))
        screen.blit(irg_text3, (10, 105))
        screen.blit(irg_text4, (10, 135))
        screen.blit(irg_text5, (10, 165))
        screen.blit(irg_text6, (10, 195))
        screen.blit(irg_text7, (10, 225))
        screen.blit(irg_text8, (10, 255))
        screen.blit(irg_text9, (10, 285))
        screen.blit(irg_text10, (10, 315))
        screen.blit(irg_text11, (10, 345))
        screen.blit(irg_text12, (10, 375))
    elif hvk_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_bool = False
            hvk_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(hvk_image, hvk_image_rect)
        pg.draw.rect(screen, (152, 245, 255), hvk_image_rect, width=5, border_radius=25)
        screen.blit(hvk_title, (10, 30))
        screen.blit(hvk_text, (10, 75))
        screen.blit(hvk_text2, (10, 105))
        screen.blit(hvk_text3, (10, 135))
        screen.blit(hvk_text4, (10, 165))
        screen.blit(hvk_text5, (10, 195))
        screen.blit(hvk_text6, (10, 225))
        screen.blit(hvk_text7, (10, 255))
        screen.blit(hvk_text8, (10, 285))
    elif usvn_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_bool = False
            usvn_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back, back_rect)
        screen.blit(back2, back_rect2)
        screen.blit(usvn_image, usvn_image_rect)
        pg.draw.rect(screen, (152, 245, 255), usvn_image_rect, width=5, border_radius=20)
        screen.blit(usvn_title, (10, 30))
        screen.blit(usvn_text, (10, 75))
        screen.blit(usvn_text2, (10, 105))
        screen.blit(usvn_text3, (10, 135))
        screen.blit(usvn_text4, (10, 165))
        screen.blit(usvn_text5, (10, 195))
        screen.blit(usvn_text6, (10, 225))
        screen.blit(usvn_text7, (10, 255))
        screen.blit(usvn_text8, (10, 285))
        screen.blit(usvn_text9, (10, 315))
    elif bvg_bool:
        check_bool = True
        if back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_bool = False
            check_bool = False
            click.play(0)
        elif back_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_bool = False
            bvg_quiz = True
            click.play(0)
        pg.draw.line(screen, (234, 234, 234), (0, 25), (1460, 25))
        pg.draw.line(screen, (234, 234, 234), (0, 875), (1460, 875))
        screen.blit(back2, back_rect2)
        screen.blit(bvg_image, bvg_image_rect)
        pg.draw.rect(screen, (152, 245, 255), bvg_image_rect, width=5, border_radius=10)
        screen.blit(bvg_title, (10, 30))
        screen.blit(bvg_text, (10, 75))
        screen.blit(bvg_text2, (10, 105))
        screen.blit(bvg_text3, (10, 135))
        screen.blit(bvg_text4, (10, 165))
        screen.blit(bvg_text5, (10, 195))
        screen.blit(bvg_text6, (10, 225))
        screen.blit(bvg_text7, (10, 255))
        screen.blit(bvg_text8, (10, 285))
        screen.blit(bvg_text9, (10, 315))
        screen.blit(bvg_text10, (10, 345))
        screen.blit(bvg_text11, (10, 375))
        screen.blit(bvg_text12, (10, 405))
        screen.blit(bvg_text13, (10, 435))
        screen.blit(bvg_text14, (10, 465))
        screen.blit(bvg_text15, (10, 495))
        screen.blit(bvg_text16, (10, 525))
        screen.blit(bvg_text17, (10, 555))
        screen.blit(bvg_text18, (10, 585))
        screen.blit(bvg_text19, (10, 615))
        screen.blit(bvg_text20, (10, 645))
    if mvm_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_quiz = False
            mvm_bool = True
            click.play(0)
        screen.blit(quiz_title, (605, 5))
        screen.blit(mvm_quiz_image, mvm_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), mvm_quiz_image_rect, width=5, border_radius=25)
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if mvm_quiz1_text_rect2.collidepoint(mouse) or mvm_quiz1_text_rect3.collidepoint(mouse) or mvm_quiz1_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mvm_quiz1_wrong = True
                mvm_quiz1_right = False
                wrong_sound.play(0)
        elif mvm_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_quiz1_right = True
            mvm_quiz1_wrong = False
            right_sound.play(0)
        if mvm_quiz1_wrong:
            screen.blit(wrong, (593, 285))
            while mvm1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm1wrong = 1
        elif mvm_quiz1_right:
            screen.blit(right, (593, 285))
            while mvm1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(mvm_quiz1, (583, 155))
        screen.blit(mvm_quiz1_2, (583, 175))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(mvm_quiz1_text, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(mvm_quiz1_text2, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(mvm_quiz1_text3, (593, 245))
        pg.draw.circle(screen, (234, 234, 234), (583, 275), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 275), 3)
        screen.blit(mvm_quiz1_text4, (593, 265))
        # Question 2
        if mvm_quiz2_text_rect.collidepoint(mouse) or mvm_quiz2_text_rect3.collidepoint(mouse) or mvm_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mvm_quiz2_wrong = True
                mvm_quiz2_right = False
                wrong_sound.play(0)
        elif mvm_quiz2_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_quiz2_right = True
            mvm_quiz2_wrong = False
            right_sound.play(0)
        if mvm_quiz2_wrong:
            screen.blit(wrong, (593, 520))
            while mvm2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm2wrong = 1
        elif mvm_quiz2_right:
            screen.blit(right, (593, 520))
            while mvm2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(mvm_quiz2, (583, 370))
        screen.blit(mvm_quiz2_2, (583, 390))
        screen.blit(mvm_quiz2_3, (583, 410))
        pg.draw.circle(screen, (234, 234, 234), (583, 450), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 450), 3)
        screen.blit(mvm_quiz2_text, (593, 440))
        pg.draw.circle(screen, (234, 234, 234), (583, 470), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 470), 3)
        screen.blit(mvm_quiz2_text2, (593, 460))
        pg.draw.circle(screen, (234, 234, 234), (583, 490), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 490), 3)
        screen.blit(mvm_quiz2_text3, (593, 480))
        pg.draw.circle(screen, (234, 234, 234), (583, 510), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 510), 3)
        screen.blit(mvm_quiz2_text4, (593, 500))
        # Question 3
        if mvm_quiz3_text_rect.collidepoint(mouse) or mvm_quiz3_text_rect2.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mvm_quiz3_wrong = True
                mvm_quiz3_right = False
                wrong_sound.play(0)
        elif mvm_quiz3_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_quiz3_right = True
            mvm_quiz3_wrong = False
            right_sound.play(0)
        if mvm_quiz3_wrong:
            screen.blit(wrong, (254, 415))
            while mvm3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm3wrong = 1
        elif mvm_quiz3_right:
            screen.blit(right, (254, 415))
            while mvm3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(mvm_quiz3, (244, 255))
        screen.blit(mvm_quiz3_2, (244, 275))
        screen.blit(mvm_quiz3_3, (244, 295))
        screen.blit(mvm_quiz3_4, (244, 315))
        screen.blit(mvm_quiz3_5, (244, 335))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(mvm_quiz3_text, (254, 365))
        pg.draw.circle(screen, (234, 234, 234), (244, 395), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 395), 3)
        screen.blit(mvm_quiz3_text2, (254, 385))
        pg.draw.circle(screen, (234, 234, 234), (244, 415), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 415), 3)
        screen.blit(mvm_quiz3_text3, (254, 405))
        # Question 4
        if mvm_quiz4_text_rect.collidepoint(mouse) or mvm_quiz4_text_rect3.collidepoint(mouse) or mvm_quiz4_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mvm_quiz4_wrong = True
                mvm_quiz4_right = False
                wrong_sound.play(0)
        elif mvm_quiz4_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mvm_quiz4_right = True
            mvm_quiz4_wrong = False
            right_sound.play(0)
        if mvm_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while mvm4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm4wrong = 1
        elif mvm_quiz4_right:
            screen.blit(right, (932, 385))
            while mvm4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mvm4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(mvm_quiz4, (922, 255))
        screen.blit(mvm_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(mvm_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(mvm_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(mvm_quiz4_text3, (932, 345))
        pg.draw.circle(screen, (234, 234, 234), (922, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 375), 3)
        screen.blit(mvm_quiz4_text4, (932, 365))
    elif pvf_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz = False
            pvf_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(pvf_quiz_image, pvf_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), pvf_quiz_image_rect, width=5, border_radius=35)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if pvf_quiz1_text_rect.collidepoint(mouse) or pvf_quiz1_text_rect2.collidepoint(mouse) or pvf_quiz1_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                pvf_quiz1_wrong = True
                pvf_quiz1_right = False
                wrong_sound.play(0)
        elif pvf_quiz1_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz1_right = True
            pvf_quiz1_wrong = False
            right_sound.play(0)
        if pvf_quiz1_wrong:
            screen.blit(wrong, (593, 285))
            while pvf1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf1wrong = 1
        elif pvf_quiz1_right:
            screen.blit(right, (593, 285))
            while pvf1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(pvf_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(pvf_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(pvf_quiz1_text2, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(pvf_quiz1_text3, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(pvf_quiz1_text4, (593, 245))
        # Question 2
        if pvf_quiz2_text_rect2.collidepoint(mouse) or pvf_quiz2_text_rect3.collidepoint(mouse) or pvf_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                pvf_quiz2_wrong = True
                pvf_quiz2_right = False
                wrong_sound.play(0)
        elif pvf_quiz2_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz2_right = True
            pvf_quiz2_wrong = False
            right_sound.play(0)
        if pvf_quiz2_wrong:
            screen.blit(wrong, (593, 520))
            while pvf2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf2wrong = 1
        elif pvf_quiz2_right:
            screen.blit(right, (593, 520))
            while pvf2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(pvf_quiz2, (583, 370))
        screen.blit(pvf_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 420), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 420), 3)
        screen.blit(pvf_quiz2_text, (593, 410))
        pg.draw.circle(screen, (234, 234, 234), (583, 440), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 440), 3)
        screen.blit(pvf_quiz2_text2, (593, 430))
        pg.draw.circle(screen, (234, 234, 234), (583, 460), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 460), 3)
        screen.blit(pvf_quiz2_text3, (593, 450))
        pg.draw.circle(screen, (234, 234, 234), (583, 480), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 480), 3)
        screen.blit(pvf_quiz2_text4, (593, 470))
        # Question 3
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(pvf_quiz3, (244, 255))
        screen.blit(pvf_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(pvf_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(pvf_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(pvf_quiz3_text3, (254, 345))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(pvf_quiz3_text4, (254, 365))
        if pvf_quiz3_text_rect.collidepoint(mouse) or pvf_quiz3_text_rect2.collidepoint(mouse) or pvf_quiz3_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                pvf_quiz3_wrong = True
                pvf_quiz3_right = False
                wrong_sound.play(0)
        elif pvf_quiz3_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz3_right = True
            pvf_quiz3_wrong = False
            right_sound.play(0)
        if pvf_quiz3_wrong:
            screen.blit(wrong, (254, 415))
            while pvf3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf3wrong = 1
        elif pvf_quiz3_right:
            screen.blit(right, (254, 415))
            while pvf3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf3right = 1
        # Question 4
        if pvf_quiz4_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz4_wrong = True
            pvf_quiz4_right = False
            wrong_sound.play(0)
        elif pvf_quiz4_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            pvf_quiz4_right = True
            pvf_quiz4_wrong = False
            right_sound.play(0)
        if pvf_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while pvf4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf4wrong = 1
        elif pvf_quiz4_right:
            screen.blit(right, (932, 385))
            while pvf4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                pvf4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(pvf_quiz4, (922, 255))
        screen.blit(pvf_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(pvf_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(pvf_quiz4_text2, (932, 325))
    elif bvb_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz = False
            bvb_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(bvb_quiz_image, bvb_quiz_image_rect)
        pg.draw.circle(screen, (152, 245, 255), (730, 700), 93, width=10)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if bvb_quiz1_text_rect.collidepoint(mouse) or bvb_quiz1_text_rect2.collidepoint(mouse) or bvb_quiz1_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvb_quiz1_wrong = True
                bvb_quiz1_right = False
                wrong_sound.play(0)
        elif bvb_quiz1_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz1_right = True
            bvb_quiz1_wrong = False
            right_sound.play(0)
        if bvb_quiz1_wrong:
            screen.blit(wrong, (593, 285))
            while bvb1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb1wrong = 1
        elif bvb_quiz1_right:
            screen.blit(right, (593, 285))
            while bvb1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(bvb_quiz1, (583, 155))
        screen.blit(bvb_quiz1_2, (583, 175))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(bvb_quiz1_text, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(bvb_quiz1_text2, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(bvb_quiz1_text3, (593, 245))
        pg.draw.circle(screen, (234, 234, 234), (583, 275), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 275), 3)
        screen.blit(bvb_quiz1_text4, (593, 265))
        # Question 2
        if bvb_quiz2_text_rect.collidepoint(mouse) or bvb_quiz2_text_rect3.collidepoint(mouse) or bvb_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvb_quiz2_wrong = True
                bvb_quiz2_right = False
                wrong_sound.play(0)
        elif bvb_quiz2_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz2_right = True
            bvb_quiz2_wrong = False
            right_sound.play(0)
        if bvb_quiz2_wrong:
            screen.blit(wrong, (593, 505))
            while bvb2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb2wrong = 1
        elif bvb_quiz2_right:
            screen.blit(right, (593, 505))
            while bvb2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(bvb_quiz2, (583, 370))
        screen.blit(bvb_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(bvb_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(bvb_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(bvb_quiz2_text3, (593, 465))
        pg.draw.circle(screen, (234, 234, 234), (583, 495), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 495), 3)
        screen.blit(bvb_quiz2_text4, (593, 485))
        # Question 3
        if bvb_quiz3_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz3_wrong = True
            bvb_quiz3_right = False
            wrong_sound.play(0)
        elif bvb_quiz3_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz3_right = True
            bvb_quiz3_wrong = False
            right_sound.play(0)
        if bvb_quiz3_wrong:
            screen.blit(wrong, (254, 325))
            while bvb3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb3wrong = 1
        elif bvb_quiz3_right:
            screen.blit(right, (254, 325))
            while bvb3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(bvb_quiz3, (244, 255))
        pg.draw.circle(screen, (234, 234, 234), (244, 295), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 295), 3)
        screen.blit(bvb_quiz3_text, (254, 285))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(bvb_quiz3_text2, (254, 305))
        # Question 4
        if bvb_quiz4_text_rect.collidepoint(mouse) or bvb_quiz4_text_rect2.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvb_quiz4_wrong = True
                bvb_quiz4_right = False
                wrong_sound.play(0)
        elif bvb_quiz4_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvb_quiz4_right = True
            bvb_quiz4_wrong = False
            right_sound.play(0)
        if bvb_quiz4_wrong:
            screen.blit(wrong, (932, 365))
            while bvb4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb4wrong = 1
        elif bvb_quiz4_right:
            screen.blit(right, (932, 365))
            while bvb4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvb4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(bvb_quiz4, (922, 255))
        screen.blit(bvb_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(bvb_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(bvb_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(bvb_quiz4_text3, (932, 345))
    elif gvw_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_quiz = False
            gvw_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(gvw_quiz_image, gvw_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), gvw_quiz_image_rect, width=5, border_radius=25)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if gvw_quiz1_text_rect.collidepoint(mouse) or gvw_quiz1_text_rect2.collidepoint(mouse) or gvw_quiz1_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                gvw_quiz1_wrong = True
                gvw_quiz1_right = False
                wrong_sound.play(0)
        elif gvw_quiz1_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_quiz1_right = True
            gvw_quiz1_wrong = False
            right_sound.play(0)
        if gvw_quiz1_wrong:
            screen.blit(wrong, (593, 265))
            while gvw1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw1wrong = 1
        elif gvw_quiz1_right:
            screen.blit(right, (593, 265))
            while gvw1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(gvw_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(gvw_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(gvw_quiz1_text2, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(gvw_quiz1_text3, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(gvw_quiz1_text4, (593, 245))
        # Question 2
        if gvw_quiz2_text_rect2.collidepoint(mouse) or gvw_quiz2_text_rect3.collidepoint(mouse) or gvw_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                gvw_quiz2_wrong = True
                gvw_quiz2_right = False
                wrong_sound.play(0)
        elif gvw_quiz2_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_quiz2_right = True
            gvw_quiz2_wrong = False
            right_sound.play(0)
        if gvw_quiz2_wrong:
            screen.blit(wrong, (593, 505))
            while gvw2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw2wrong = 1
        elif gvw_quiz2_right:
            screen.blit(right, (593, 505))
            while gvw2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(gvw_quiz2, (583, 370))
        screen.blit(gvw_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(gvw_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(gvw_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(gvw_quiz2_text3, (593, 465))
        pg.draw.circle(screen, (234, 234, 234), (583, 495), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 495), 3)
        screen.blit(gvw_quiz2_text4, (593, 485))
        # Question 3
        if gvw_quiz3_text_rect.collidepoint(mouse) or gvw_quiz3_text_rect2.collidepoint(mouse) or gvw_quiz3_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                gvw_quiz3_wrong = True
                gvw_quiz3_right = False
                wrong_sound.play(0)
        elif gvw_quiz3_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_quiz3_right = True
            gvw_quiz3_wrong = False
            right_sound.play(0)
        if gvw_quiz3_wrong:
            screen.blit(wrong, (254, 385))
            while gvw3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw3wrong = 1
        elif gvw_quiz3_right:
            screen.blit(right, (254, 385))
            while gvw3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(gvw_quiz3, (244, 255))
        screen.blit(gvw_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(gvw_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(gvw_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(gvw_quiz3_text3, (254, 345))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(gvw_quiz3_text4, (254, 365))
        # Question 4
        if gvw_quiz4_text_rect.collidepoint(mouse) or gvw_quiz4_text_rect3.collidepoint(mouse) or gvw_quiz4_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                gvw_quiz4_wrong = True
                gvw_quiz4_right = False
                wrong_sound.play(0)
        elif gvw_quiz4_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            gvw_quiz4_right = True
            gvw_quiz4_wrong = False
            right_sound.play(0)
        if gvw_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while gvw4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw4wrong = 1
        elif gvw_quiz4_right:
            screen.blit(right, (932, 385))
            while gvw4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                gvw4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(gvw_quiz4, (922, 255))
        screen.blit(gvw_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(gvw_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(gvw_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(gvw_quiz4_text3, (932, 345))
        pg.draw.circle(screen, (234, 234, 234), (922, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 375), 3)
        screen.blit(gvw_quiz4_text4, (932, 365))
    elif mva_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz = False
            mva_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(mva_quiz_image, mva_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), mva_quiz_image_rect, width=5, border_radius=25)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if mva_quiz1_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz1_wrong = True
            mva_quiz1_right = False
            wrong_sound.play(0)
        elif mva_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz1_right = True
            mva_quiz1_wrong = False
            right_sound.play(0)
        if mva_quiz1_wrong:
            screen.blit(wrong, (593, 225))
            while mva1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva1wrong = 1
        elif mva_quiz1_right:
            screen.blit(right, (593, 225))
            while mva1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(mva_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(mva_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(mva_quiz1_text2, (593, 205))
        # Question 2
        if mva_quiz2_text_rect2.collidepoint(mouse) or mva_quiz2_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mva_quiz2_wrong = True
                mva_quiz2_right = False
                wrong_sound.play(0)
        elif mva_quiz2_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz2_right = True
            mva_quiz2_wrong = False
            right_sound.play(0)
        if mva_quiz2_wrong:
            screen.blit(wrong, (593, 485))
            while mva2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva2wrong = 1
        elif mva_quiz2_right:
            screen.blit(right, (593, 485))
            while mva2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(mva_quiz2, (583, 370))
        screen.blit(mva_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(mva_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(mva_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(mva_quiz2_text3, (593, 465))
        # Question 3
        if mva_quiz3_text_rect.collidepoint(mouse) or mva_quiz3_text_rect2.collidepoint(mouse) or mva_quiz3_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mva_quiz3_wrong = True
                mva_quiz3_right = False
                wrong_sound.play(0)
        elif mva_quiz3_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz3_right = True
            mva_quiz3_wrong = False
            right_sound.play(0)
        if mva_quiz3_wrong:
            screen.blit(wrong, (254, 385))
            while mva3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva3wrong = 1
        elif mva_quiz3_right:
            screen.blit(right, (254, 385))
            while mva3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(mva_quiz3, (244, 255))
        screen.blit(mva_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(mva_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(mva_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(mva_quiz3_text3, (254, 345))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(mva_quiz3_text4, (254, 365))
        # Question 4
        if mva_quiz4_text_rect.collidepoint(mouse) or mva_quiz4_text_rect3.collidepoint(mouse) or mva_quiz4_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                mva_quiz4_wrong = True
                mva_quiz4_right = False
                wrong_sound.play(0)
        elif mva_quiz4_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            mva_quiz4_right = True
            mva_quiz4_wrong = False
            right_sound.play(0)
        if mva_quiz4_wrong:
            screen.blit(wrong, (932, 365))
            while mva4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva4wrong = 1
        elif mva_quiz4_right:
            screen.blit(right, (932, 365))
            while mva2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                mva4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(mva_quiz4, (922, 255))
        pg.draw.circle(screen, (234, 234, 234), (922, 295), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 295), 3)
        screen.blit(mva_quiz4_text, (932, 285))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(mva_quiz4_text2, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(mva_quiz4_text3, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(mva_quiz4_text4, (932, 345))
    elif tvd_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz = False
            tvd_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(tvd_quiz_image, tvd_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), tvd_quiz_image_rect, width=5, border_radius=15)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if tvd_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz1_wrong = True
            tvd_quiz1_right = False
            wrong_sound.play(0)
        elif tvd_quiz1_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz1_right = True
            tvd_quiz1_wrong = False
            right_sound.play(0)
        if tvd_quiz1_wrong:
            screen.blit(wrong, (593, 225))
            while tvd1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd1wrong = 1
        elif tvd_quiz1_right:
            screen.blit(right, (593, 225))
            while tvd1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(tvd_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(tvd_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(tvd_quiz1_text2, (593, 205))
        # Question 2
        if tvd_quiz2_text_rect.collidepoint(mouse) or tvd_quiz2_text_rect2.collidepoint(mouse) or tvd_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                tvd_quiz2_wrong = True
                tvd_quiz2_right = False
                wrong_sound.play(0)
        elif tvd_quiz2_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz2_right = True
            tvd_quiz2_wrong = False
            right_sound.play(0)
        if tvd_quiz2_wrong:
            screen.blit(wrong, (593, 485))
            while tvd2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd2wrong = 1
        elif tvd_quiz2_right:
            screen.blit(right, (593, 485))
            while tvd2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(tvd_quiz2, (583, 370))
        pg.draw.circle(screen, (234, 234, 234), (583, 415), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 415), 3)
        screen.blit(tvd_quiz2_text, (593, 405))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(tvd_quiz2_text2, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(tvd_quiz2_text3, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(tvd_quiz2_text4, (593, 465))
        # Question 3
        if tvd_quiz3_text_rect.collidepoint(mouse) or tvd_quiz3_text_rect2.collidepoint(mouse) or tvd_quiz3_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                tvd_quiz3_wrong = True
                tvd_quiz3_right = False
                wrong_sound.play(0)
        elif tvd_quiz3_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz3_right = True
            tvd_quiz3_wrong = False
            right_sound.play(0)
        if tvd_quiz3_wrong:
            screen.blit(wrong, (254, 385))
            while tvd3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd3wrong = 1
        elif tvd_quiz3_right:
            screen.blit(right, (254, 385))
            while tvd3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(tvd_quiz3, (244, 255))
        screen.blit(tvd_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(tvd_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(tvd_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(tvd_quiz3_text3, (254, 345))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(tvd_quiz3_text4, (254, 365))
        # Question 4
        if tvd_quiz4_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz4_wrong = True
            tvd_quiz4_right = False
            wrong_sound.play(0)
        elif tvd_quiz4_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            tvd_quiz4_right = True
            tvd_quiz4_wrong = False
            right_sound.play(0)
        if tvd_quiz4_wrong:
            screen.blit(wrong, (932, 365))
            while tvd4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd4wrong = 1
        elif tvd_quiz4_right:
            screen.blit(right, (932, 365))
            while tvd4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                tvd4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(tvd_quiz4, (922, 255))
        screen.blit(tvd_quiz4_2, (922, 275))
        screen.blit(tvd_quiz4_3, (922, 295))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(tvd_quiz4_text, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(tvd_quiz4_text2, (932, 345))
    elif irg_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_quiz = False
            irg_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(irg_quiz_image, irg_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), irg_quiz_image_rect, width=5, border_radius=15)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if irg_quiz1_text_rect2.collidepoint(mouse) or irg_quiz1_text_rect3.collidepoint(mouse) or irg_quiz1_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                irg_quiz1_wrong = True
                irg_quiz1_right = False
                wrong_sound.play(0)
        elif irg_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_quiz1_right = True
            irg_quiz1_wrong = False
            right_sound.play(0)
        if irg_quiz1_wrong:
            screen.blit(wrong, (593, 265))
            while irg1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg1wrong = 1
        elif irg_quiz1_right:
            screen.blit(right, (593, 265))
            while irg1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(irg_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(irg_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(irg_quiz1_text2, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(irg_quiz1_text3, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(irg_quiz1_text4, (593, 245))
        # Question 2
        if irg_quiz2_text_rect.collidepoint(mouse) or irg_quiz2_text_rect2.collidepoint(mouse) or irg_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                irg_quiz2_wrong = True
                irg_quiz2_right = False
                wrong_sound.play(0)
        elif irg_quiz2_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_quiz2_right = True
            irg_quiz2_wrong = False
            right_sound.play(0)
        if irg_quiz2_wrong:
            screen.blit(wrong, (593, 505))
            while irg2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg2wrong = 1
        elif irg_quiz2_right:
            screen.blit(right, (593, 505))
            while irg2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(irg_quiz2, (583, 370))
        screen.blit(irg_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(irg_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(irg_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(irg_quiz2_text3, (593, 465))
        pg.draw.circle(screen, (234, 234, 234), (583, 495), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 495), 3)
        screen.blit(irg_quiz2_text4, (593, 485))
        # Question 3
        if irg_quiz3_text_rect.collidepoint(mouse) or irg_quiz3_text_rect2.collidepoint(mouse) or irg_quiz3_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                irg_quiz3_wrong = True
                irg_quiz3_right = False
                wrong_sound.play(0)
        elif irg_quiz3_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_quiz3_right = True
            irg_quiz3_wrong = False
            right_sound.play(0)
        if irg_quiz3_wrong:
            screen.blit(wrong, (254, 385))
            while irg3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg3wrong = 1
        elif irg_quiz3_right:
            screen.blit(right, (254, 385))
            while irg3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(irg_quiz3, (244, 255))
        screen.blit(irg_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(irg_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(irg_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(irg_quiz3_text3, (254, 345))
        pg.draw.circle(screen, (234, 234, 234), (244, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 375), 3)
        screen.blit(irg_quiz3_text4, (254, 365))
        # Question 4
        if irg_quiz4_text_rect.collidepoint(mouse) or irg_quiz4_text_rect2.collidepoint(mouse) or irg_quiz4_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                irg_quiz4_wrong = True
                irg_quiz4_right = False
                wrong_sound.play(0)
        elif irg_quiz4_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            irg_quiz4_right = True
            irg_quiz4_wrong = False
            right_sound.play(0)
        if irg_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while irg4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg4wrong = 1
        elif irg_quiz4_right:
            screen.blit(right, (932, 385))
            while irg4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                irg4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(irg_quiz4, (922, 255))
        screen.blit(irg_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(irg_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(irg_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(irg_quiz4_text3, (932, 345))
        pg.draw.circle(screen, (234, 234, 234), (922, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 375), 3)
        screen.blit(irg_quiz4_text4, (932, 365))
    elif hvk_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_quiz = False
            hvk_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(hvk_quiz_image, hvk_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), hvk_quiz_image_rect, width=5, border_radius=10)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if hvk_quiz1_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_quiz1_wrong = True
            hvk_quiz1_right = False
            wrong_sound.play(0)
        elif hvk_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_quiz1_right = True
            hvk_quiz1_wrong = False
            right_sound.play(0)
        if hvk_quiz1_wrong:
            screen.blit(wrong, (593, 245))
            while hvk1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                hvk1wrong = 1
        elif hvk_quiz1_right:
            screen.blit(right, (593, 245))
            while hvk1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                hvk1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(hvk_quiz1, (583, 155))
        screen.blit(hvk_quiz1_2, (583, 175))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(hvk_quiz1_text, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(hvk_quiz1_text2, (593, 225))
        # Question 2
        if hvk_quiz2_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_quiz2_wrong = True
            hvk_quiz2_right = False
            wrong_sound.play(0)
        elif hvk_quiz2_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            hvk_quiz2_right = True
            hvk_quiz2_wrong = False
            right_sound.play(0)
        if hvk_quiz2_wrong:
            screen.blit(wrong, (593, 460))
            while hvk2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                hvk2wrong = 1
        elif hvk_quiz2_right:
            screen.blit(right, (593, 460))
            while hvk1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                hvk1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(hvk_quiz2, (583, 370))
        screen.blit(hvk_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 430), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 430), 3)
        screen.blit(hvk_quiz2_text, (593, 420))
        pg.draw.circle(screen, (234, 234, 234), (583, 450), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 450), 3)
        screen.blit(hvk_quiz2_text2, (593, 440))
    elif usvn_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz = False
            usvn_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(usvn_quiz_image, usvn_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), usvn_quiz_image_rect, width=5, border_radius=10)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if usvn_quiz1_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz1_wrong = True
            usvn_quiz1_right = False
            wrong_sound.play(0)
        elif usvn_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz1_right = True
            usvn_quiz1_wrong = False
            right_sound.play(0)
        if usvn_quiz1_wrong:
            screen.blit(wrong, (593, 225))
            while usvn1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn1wrong = 1
        elif usvn_quiz1_right:
            screen.blit(right, (593, 225))
            while usvn1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(usvn_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(usvn_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(usvn_quiz1_text2, (593, 205))
        # Question 2
        if usvn_quiz2_text_rect2.collidepoint(mouse) or usvn_quiz2_text_rect3.collidepoint(mouse) or usvn_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                usvn_quiz2_wrong = True
                usvn_quiz2_right = False
                wrong_sound.play(0)
        elif usvn_quiz2_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz2_right = True
            usvn_quiz2_wrong = False
            right_sound.play(0)
        if usvn_quiz2_wrong:
            screen.blit(wrong, (593, 505))
            while usvn2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn2wrong = 1
        elif usvn_quiz2_right:
            screen.blit(right, (593, 505))
            while usvn2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(usvn_quiz2, (583, 370))
        screen.blit(usvn_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(usvn_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(usvn_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(usvn_quiz2_text3, (593, 465))
        pg.draw.circle(screen, (234, 234, 234), (583, 495), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 495), 3)
        screen.blit(usvn_quiz2_text4, (593, 485))
        # Question 3
        if usvn_quiz3_text_rect2.collidepoint(mouse) or usvn_quiz3_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                usvn_quiz3_wrong = True
                usvn_quiz3_right = False
                wrong_sound.play(0)
        elif usvn_quiz3_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz3_right = True
            usvn_quiz3_wrong = False
            right_sound.play(0)
        if usvn_quiz3_wrong:
            screen.blit(wrong, (254, 365))
            while usvn3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn3wrong = 1
        elif usvn_quiz3_right:
            screen.blit(right, (254, 365))
            while usvn3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(usvn_quiz3, (244, 255))
        screen.blit(usvn_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(usvn_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(usvn_quiz3_text2, (254, 325))
        pg.draw.circle(screen, (234, 234, 234), (244, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 355), 3)
        screen.blit(usvn_quiz3_text3, (254, 345))
        # Question 4
        if usvn_quiz4_text_rect.collidepoint(mouse) or usvn_quiz4_text_rect2.collidepoint(mouse) or usvn_quiz4_text_rect3.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                usvn_quiz4_wrong = True
                usvn_quiz4_right = False
                wrong_sound.play(0)
        elif usvn_quiz4_text_rect4.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            usvn_quiz4_right = True
            usvn_quiz4_wrong = False
            right_sound.play(0)
        if usvn_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while usvn4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn4wrong = 1
        elif usvn_quiz4_right:
            screen.blit(right, (932, 385))
            while usvn4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                usvn4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(usvn_quiz4, (922, 255))
        screen.blit(usvn_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(usvn_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(usvn_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(usvn_quiz4_text3, (932, 345))
        pg.draw.circle(screen, (234, 234, 234), (922, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 375), 3)
        screen.blit(usvn_quiz4_text4, (932, 365))
    elif bvg_quiz:
        if big_back_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz = False
            bvg_bool = True
            click.play(0)
        screen.blit(quiz_title, (600, 5))
        screen.blit(big_back, big_back_rect)
        pg.draw.line(screen, (234, 234, 234), (0, 100), (1460, 100))
        pg.draw.line(screen, (234, 234, 234), (0, 800), (1460, 800))
        screen.blit(bvg_quiz_image, bvg_quiz_image_rect)
        pg.draw.rect(screen, (152, 245, 255), bvg_quiz_image_rect, width=5, border_radius=10)
        pg.draw.rect(screen, (227, 207, 87), (15, 115, 400, 18), border_radius=10)
        screen.blit(tokens_text, (30, 115))
        screen.blit(tokens_text2, (100, 115))
        # Question 1
        if bvg_quiz1_text_rect2.collidepoint(mouse) or bvg_quiz1_text_rect3.collidepoint(mouse) or bvg_quiz1_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvg_quiz1_wrong = True
                bvg_quiz1_right = False
                wrong_sound.play(0)
        elif bvg_quiz1_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz1_right = True
            bvg_quiz1_wrong = False
            right_sound.play(0)
        if bvg_quiz1_wrong:
            screen.blit(wrong, (593, 265))
            while bvg1wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg1wrong = 1
        elif bvg_quiz1_right:
            screen.blit(right, (593, 265))
            while bvg1right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg1right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 150, 324, 200), width=5, border_radius=25)
        screen.blit(bvg_quiz1, (583, 155))
        pg.draw.circle(screen, (234, 234, 234), (583, 195), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 195), 3)
        screen.blit(bvg_quiz1_text, (593, 185))
        pg.draw.circle(screen, (234, 234, 234), (583, 215), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 215), 3)
        screen.blit(bvg_quiz1_text2, (593, 205))
        pg.draw.circle(screen, (234, 234, 234), (583, 235), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 235), 3)
        screen.blit(bvg_quiz1_text3, (593, 225))
        pg.draw.circle(screen, (234, 234, 234), (583, 255), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 255), 3)
        screen.blit(bvg_quiz1_text4, (593, 245))
        # Question 2
        if bvg_quiz2_text_rect.collidepoint(mouse) or bvg_quiz2_text_rect2.collidepoint(mouse) or bvg_quiz2_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvg_quiz2_wrong = True
                bvg_quiz2_right = False
                wrong_sound.play(0)
        elif bvg_quiz2_text_rect3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz2_right = True
            bvg_quiz2_wrong = False
            right_sound.play(0)
        if bvg_quiz2_wrong:
            screen.blit(wrong, (593, 505))
            while bvg2wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg2wrong = 1
        elif bvg_quiz2_right:
            screen.blit(right, (593, 505))
            while bvg2right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg2right = 1
        pg.draw.rect(screen, (234, 234, 234), (568, 365, 324, 200), width=5, border_radius=25)
        screen.blit(bvg_quiz2, (583, 370))
        screen.blit(bvg_quiz2_2, (583, 390))
        pg.draw.circle(screen, (234, 234, 234), (583, 435), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 435), 3)
        screen.blit(bvg_quiz2_text, (593, 425))
        pg.draw.circle(screen, (234, 234, 234), (583, 455), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 455), 3)
        screen.blit(bvg_quiz2_text2, (593, 445))
        pg.draw.circle(screen, (234, 234, 234), (583, 475), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 475), 3)
        screen.blit(bvg_quiz2_text3, (593, 465))
        pg.draw.circle(screen, (234, 234, 234), (583, 495), 5)
        pg.draw.circle(screen, (152, 245, 255), (583, 495), 3)
        screen.blit(bvg_quiz2_text4, (593, 485))
        # Question 3
        if bvg_quiz3_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz3_wrong = True
            bvg_quiz3_right = False
            wrong_sound.play(0)
        elif bvg_quiz3_text_rect2.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz3_right = True
            bvg_quiz3_wrong = False
            right_sound.play(0)
        if bvg_quiz3_wrong:
            screen.blit(wrong, (254, 345))
            while bvg3wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg3wrong = 1
        elif bvg_quiz3_right:
            screen.blit(right, (254, 345))
            while bvg3right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg3right = 1
        pg.draw.rect(screen, (234, 234, 234), (229, 250, 324, 200), width=5, border_radius=25)
        screen.blit(bvg_quiz3, (244, 255))
        screen.blit(bvg_quiz3_2, (244, 275))
        pg.draw.circle(screen, (234, 234, 234), (244, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 315), 3)
        screen.blit(bvg_quiz3_text, (254, 305))
        pg.draw.circle(screen, (234, 234, 234), (244, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (244, 335), 3)
        screen.blit(bvg_quiz3_text2, (254, 325))
        # Question 4
        if bvg_quiz4_text_rect2.collidepoint(mouse) or bvg_quiz4_text_rect3.collidepoint(mouse) or bvg_quiz4_text_rect4.collidepoint(mouse):
            if event.type == pg.MOUSEBUTTONDOWN:
                bvg_quiz4_wrong = True
                bvg_quiz4_right = False
                wrong_sound.play(0)
        elif bvg_quiz4_text_rect.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            bvg_quiz4_right = True
            bvg_quiz4_wrong = False
            right_sound.play(0)
        if bvg_quiz4_wrong:
            screen.blit(wrong, (932, 385))
            while bvg4wrong == 0:
                tokens -= 1
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg4wrong = 1
        elif bvg_quiz4_right:
            screen.blit(right, (932, 385))
            while bvg4right == 0:
                tokens += 4
                tokens_text2 = font.render(f"{tokens}", True, (0, 0, 0))
                bvg4right = 1
        pg.draw.rect(screen, (234, 234, 234), (907, 250, 324, 200), width=5, border_radius=25)
        screen.blit(bvg_quiz4, (922, 255))
        screen.blit(bvg_quiz4_2, (922, 275))
        pg.draw.circle(screen, (234, 234, 234), (922, 315), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 315), 3)
        screen.blit(bvg_quiz4_text, (932, 305))
        pg.draw.circle(screen, (234, 234, 234), (922, 335), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 335), 3)
        screen.blit(bvg_quiz4_text2, (932, 325))
        pg.draw.circle(screen, (234, 234, 234), (922, 355), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 355), 3)
        screen.blit(bvg_quiz4_text3, (932, 345))
        pg.draw.circle(screen, (234, 234, 234), (922, 375), 5)
        pg.draw.circle(screen, (152, 245, 255), (922, 375), 3)
        screen.blit(bvg_quiz4_text4, (932, 365))
    if play:
        pg.draw.rect(screen, (125, 158, 192), (50, 50, 486, 800), border_radius=25)
        pg.draw.rect(screen, (234, 234, 234), (50, 50, 486, 800), width=5, border_radius=25)
        time_font = pg.font.Font(None, 50)
        time_render2 = time_font.render(f"{round((pg.time.get_ticks()) / 100) / 10}", True, (0, 100, 0))
        screen.blit(time_render2, (75, 75))
        screen.blit(cannon, (550, 450))
    pg.display.update()
    clock.tick(30)
