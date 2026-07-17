with open("example_2.txt","w") as f:
    line1="My name is Saivinay"
    line2="MY age is 21"
    line3="I am from IT background"
    line4="I am Studying S.R.K.R"
    line5="My hometown cheyyeru"
    f.writelines([line1+"\n",line2+"\n",line3+"\n",line4+"\n",line5])