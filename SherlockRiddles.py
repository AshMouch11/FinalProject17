class Sherlock(object):
    def __init__(self):
        self.riddle1 = """What is Sherlock's brothers name?
        a. Sherrinford
        b. Mycroft
        c. John
        d. Eurus
        """
        self.answer1 = 'b'
        self.riddle2 = """Where did Dr. Watson serve?
        a. Iraq
        b. Afghanistan
        c. Vietnam
        d. Iran
        """
        self.answer2 = 'b'
        self.riddle3 = """What is the name of the pathologist that frequently helps Sherlock in his cases?
        a. Harriet
        b. Holly
        c. Helen
        d. Molly
        """
        self.answer3 = 'd'
        self.riddle4 = """What was the name of the first episode of season 1 of Sherlock?
        a. The Final Problem
        b. The Blind Banker
        c. The Great Game
        d. A Study in Pink
        """
        self.answer4 = 'd'

        self.riddle5 = """What is John Watson's middle name?
        a. Henry
        b. Hamish
        c. Heath
        d. Howard
        """
        self.answer5 = 'b'

        self.riddle6 = """What was John Watson's role in the British Army?
        a. assistant surgeon
        b. chief surgeon
        c. pilot
        d. gunman
        """
        self.answer6 = 'a'

        self.riddle7 = """What is the name of John Watson's wife?
        a. Harry
        b. Molly
        c. Hanna
        d. Mary"""
        self.answer7 = 'd'

        self.riddle8 = """What instrument does Sherlock play?
        a. cello
        b. piano
        c. violin
        d. guitar
        """
        self.answer8 = 'c'

        self.riddle9 = """What is the name of John and Mary Watson's daughter?
        a. Jenna
        b. Mary
        c. Helen
        d. Rosamund
        """
        self.answer9 = 'd'

        self.riddle10 = """Which person on the police force does Sherlock typically work with?
        a. Lestrade
        b. Anderson
        c. Moriarty
        d. Adler
        """
        self.answer10 = 'a'

        self.riddle11 = """What commonly known fact about space does Sherlock forget?
        a. the Earth is round
        b. Earth is not the only planet
        c. the Earth revolves around the Sun
        d. Earth is a part of the solar system
        """
        self.answer11 = 'c'

        self.riddle12 = """What really was Appledore?
        a. a castle
        b. a file
        c. a mind palace
        d. a computer
        """
        self.answer12 = 'c'

        self.riddle13 = """Which of the following was not one of the proposed methods of Sherlock's surviving his jump from the roof of a building?
        a. Sherlock jumped onto an airmattress.
        b. Sherlock never jumped; he used his sister's mind control powers, to convince John that he had.
        c. Sherlock bungee-jumped.
        d. Sherlock pushed a body with a mask of his face off the side of the building.
        """
        self.answer13 = 'b'

        self.riddle14 = """Where do Sherlock and John live?
        a. 122b Maker Street
        b. 212 Baker Street
        c. 221b Baker Street
        d. 221c Baker Street
        """
        self.answer14 = 'c'

        self.riddle15 = """What is the name of Sherlock's sister?
        a. Harry
        b. Eurus
        c. Mary
        d. Sherrinford
        """
        self.answer15 = 'd'

        self.riddle16 = """What article of clothing becomes the staple of Sherlock Holmes in the media?
        a. deerstalker
        b. bowler hat
        c. trench coat
        d. tie
        """
        self.answer16 = 'a'

        self.riddle17 = """What is the name of the actor that plays Sherlock Holmes?
        a. Benedict Bumberbatch
        b. Martin Freeman
        c. Mark Gatiss
        d. Andrew Scott
        """
        self.answer17 = 'a'

        self.riddle18 = """What is the name of the actor that plays John Watson?
        a. Andrew Scott
        b. Martin Freeman
        c. Benedict Cumberbatch
        d. Mark Gatiss
        """
        self.answer18 = 'b'

        self.riddle19 = """Writer of Sherlock, Mark Gatiss, also plays what character?
        a. Sherlock Holmes
        b. Mycroft Holmes
        c. John Watson
        d. Jim Moriarty
        """
        self.answer19 = 'b'

        self.riddle20 = """What is the name of Sherlock's land lady?
        a. Mrs. Hudson
        b. Mrs. Simmons
        c. Mrs. Watson
        d. Mrs. Hudderson
        """
        self.answer20 = 'a'

        self.riddle21 = """Where was John Watson shot while in the army?
        a. his leg
        b. his shoulder
        c. his stomach
        d. his elbow
        """
        self.answer21 = 'b'

        self.riddle22 = """What is the cabbie in 'A Study in Pink' suffering from?
        a. cancer
        b. dimensia
        c. gun shot wound
        d. brain aneurysm
        """
        self.answer22 = 'd'

        self.riddle23 = """What was the nationality of the pottery expert in 'The Blind Banker'?
        a. Japanese
        b. Philipino
        c. Chinese
        d. Greek
        """
        self.answer23 = 'c'

        self.riddle24 = """What is the name of the grafitti artist in 'The Blind Banker' that helps Sherlock track the spray paint?
        a. Daz
        b. Jaz
        c. Maz
        d. Raz
        """
        self.answer24 = 'd'

        self.riddle25 = """What is the surname of the man that introduces John Watson to Sherlock?
        a. Lestrade
        b. Stamford
        c. Moriarty
        d. Anderson
        """
        self.answer25 = 'b'

        self.riddle26 = """What is Jim Moriarty's ringtone?
        a. Don't Stop by 5 Seconds of Summer
        b. Photograph by Nickelback
        c. Staying Alive by the Beee Gees
        d. Stairway to Heaven by Led Zeppelin
        """
        self.answer26 = 'c'

        self.riddle27 = """Who believed Sherlock was still alive and had various theories to prove it?
        a. Greg Lestrade
        b. Molly Hooper
        c. Philip Anderson
        d. John Watson
        """
        self.answer27 = 'c'

        self.riddle28 = """What is the name of the maximum security prison facility that holds Eurus?
        a. Sherrinford
        b. Appledore
        c. Noxford
        d. Mycroford
        """
        self.answer28 = 'a'

        self.riddle29 = """What is the name Moriarty used for his actor persona?
        a. Andrew Scott
        b. Henry Knight
        c. Richard Brook
        d. Bill Wiggins
        """
        self.answer29 = 'c'

        self.riddle30 = """Who else was on the roof when Sherlock jumped from it?
        a. Irene Adler
        b. Watson
        c. Moriarty
        d. Mycroft
        """
        self.answer30 = 'c'

        self.riddle31 = """What word does Sherlock ask Mrs. Hudson to say to him if she ever believes he is being cocky?
        a. doyle
        b. soze
        c. culverton
        d. norbury
        """
        self.answer31 = 'd'

        self.riddle32 = """What is the name of Sherlock's childhood friend?
        a. Victor
        b. Henry
        c. Martin
        d. George
        """
        self.answer32 = 'a'

        self.riddle33 = """What is Mrs. Hudson's maiden name?
        a. Stubbing
        b. Sissons
        c. Simons
        d. Sallyforth
        """
        self.answer33 = 'b'

        self.riddle34 = """Who was Sherlock Holmes' greatest enemy?
        a. Moriarty
        b. Mycroft
        c. Watson
        d. Adler
        """
        self.answer34 = 'a'

        self.riddle35 = """Who is 'The Woman'?
        a. Molly Hooper
        b. his mother
        c. Eurus
        d. Irene Adler
        """
        self.answer35 = 'd'

        self.riddle36 = """What was the 4 digit passsword to Adler's phone?
        a. Lock
        b. 1895
        c. SHER
        d. 221B
        """
        self.answer36 = 'c'

        self.riddle37 = """How many nicotine patches did Sherlock need to solve his first case?
        a. 1
        b. 2
        c. 4
        d. 3
        """
        self.answer37 = 'd'

        self.riddle38 = """Who did Moriarty not threaten to kill in the name of Sherlock?
        a. Molly
        b. Mrs. Hudson
        c. Lestrade
        d. Watson
        """
        self.answer38 = 'a'

        self.riddle39 = """What is the name of John's doctor girlfriend in series 1?
        a. Sally
        b. Sophie
        c. Sammy
        d. Sarah
        """
        self.answer39 = 'd'

        self.riddle40 = """What is the minimum rating out of 10 that a case has to be for Sherlock to leave his flat for it?
        a. 7
        b. 8
        c. 6
        d. 9
        """
        self.answer40 = 'a'

        self.riddle41 = """Why did Mrs. Hudson give Sherlock such a good deal on his rent?
        a. He solved the death of her late husband.
        b. He saved her life.
        c. He helped her ex-husband get killed.
        d. He tricked her into it.
        """
        self.answer41 = 'c'

        self.riddle42 = """What's the name of John's sister?
        a. Helen
        b. Holly
        c. Harry
        d. Hannah
        """
        self.answer42 = 'c'

        self.riddle43 = """Before John, who/what did Sherlock talk through his cases with?
        a. Lestrade
        b. Mycroft
        c. his gun
        d. his skull
        """
        self.answer43 = 'd'

        self.riddle44 = """What did John's therapist suggest he do to help his PTSD?
        a. go on a date
        b. watch TV
        c. run
        d. blog
        """
        self.answer44 = 'd'

        self.riddle45 = """What was unusual about the third bomb-jacketed vitim Moriarty used to communicate with Sherlock?
        a. She was mute.
        b. She was deaf.
        c. She had only one arm.
        d. She was blind.
        """
        self.answer45 = 'd'

        self.riddle46 = """What number does John's blog hit counter get stuck on?
        a. 1873
        b. 1895
        c. 1895
        d. 1922
        """
        self.answer46 = 'c'

        self.riddle47 = """What was the name of the vanishing glow-in-the-dark rabbit?
        a. Greenball
        b. Blueball
        c. Greengirl
        d. Bluebell
        """
        self.answer47 = 'd'

        self.riddle48 = """When Sherlock and Victor played pirates as a child, what was Sherlock's nickname?
        a. Blackbeard
        b. Bluebeard
        c. Yellowbeard
        d. Redbeard
        """
        self.answer48 = 'c'

        self.riddle49 = """Where was the little girl trapped during the episode 'The Final Problem.'
        a. a well
        b. an airplane
        c. a train
        d. a car
        """
        self.answer49 = 'b'

        self.riddle50 = """Which of the following was a place that Moriarty did not break into?
        a. Bank of England
        b. Pentonville Prison
        c. Buckingham Palace
        d. The Tower of London
        """
        self.answer50 = 'c'

        self.riddle51 = """What did Sherlock save John from?
        a. poison
        b. falling off a building
        c. a fire
        d. a gunshot
        """
        self.answer51 = 'c'

        self.riddle52 = """Where did the HOUND operation take place?
        a. Sheffield, England
        b. Lawrence, Kansas
        c. Liberty, Indiana
        d. 221B Baker Street
        """
        self.answer52 = 'c'

        self.riddle53 = """When Sherlock and John play celebrity heads, who is displayed on John's forehead?
        a. Adele
        b. Sherlock Holmes
        c. Madonna
        d. Taylor Swift
        """
        self.answer53 = 'c'

        self.riddle54 = """What was the date of John and Mary Watson's marriage
        a. May 16
        b. May 17
        c. May 18
        d. May 19
        """
        self.answer54 = 'c'

        self.riddle55 = """Who ends up being the murderer at John and Mary's wedding?
        a. the caterer
        b. the photographer
        c. John's army friend
        d. the priest
        """
        self.answer55 = 'b'

        self.riddle56 = """Where did Mary shoot Sherlock?
        a. the heart
        b. between the ribs
        c. the leg
        d. the head
        """
        self.answer56 = 'b'

        self.riddle57 = """What is the Abominable Bride's real name?
        a. Emily Gianetti
        b. Florence Loretti
        c. Aurelia Moretty
        d. Emelia Ricoletti
        """
        self.answer57 = 'd'

        self.riddle58 = """What is Irene Adler's Twitter username?
        a. @thedominatrix
        b. @thewhiphand
        c. @irene_adler
        d. @thewoman
        """
        self.answer58 = 'b'

        self.riddle59 = """Which of the following was not a place where Moriarty left his 3 'IOU' messages?
        a. on John's blog
        b. on an apple
        c. the windows across from Scotland Yard
        d. a wall outside of 221B
        """
        self.answer59 = 'a'

        self.riddle60 = """What was Major Barrymore's password in The Hounds of Baskerville?
        a. Margaret
        b. Maggie
        c. Thatcher
        d. MargareThatcher
        """
        self.answer60 = 'b'
