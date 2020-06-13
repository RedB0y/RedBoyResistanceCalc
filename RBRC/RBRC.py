import argparse

digitDic={"bl":0,"br":1,"re":2,"or":3,"ye":4,"gr":5,"blu":6,"vi":7,"gre":8,"wh":9,"go":-1,"si":-2}
tolDic={"br":"+/- 1%","re":"+/- 2%","gr":"+/- 0.5%","blu":"+/- 0.25%","vi":"+/- 0.10%","gre":"+/- 0.05%","go":"+/- 5%","si":"+/- 10%"}

#print("Enter the first and last letter of the color \n eg: red = rd")

parser=argparse.ArgumentParser()
parser.add_argument("-nc",type=int,required=True,help="No Of Colors on the band")
parser.add_argument("-f",type=str,required=True,help="First color on the resistor")
parser.add_argument("-s",type=str,required=True,help="Second color on the resistor")
parser.add_argument("-t",type=str,required=True,help="Third color on the resistor")
parser.add_argument("-fo",type=str,required=True,help="Fourth color on the resistor")
parser.add_argument("--fi",type=str,default=None,help="Fifth color on the resistor")
#parser.add_argument("--si",type=str,default=None,help="Fourth color on the resistor")

args=parser.parse_args()

NoOfColors=args.nc

FirstDigit=digitDic[args.f]
SecondDigit=digitDic[args.s]

if NoOfColors == 4:
              Multiplier=10**digitDic[args.t]
              Tolerance=tolDic[args.fo]
              FirstTwoDigits=str(FirstDigit)+str(SecondDigit)

              Resis=int(FirstTwoDigits)*Multiplier
              Resis=Resis/1000

              print(Resis,"Kilo OHMS",Tolerance)
              
elif NoOfColors == 5:
              ThirdDigit=digitDic[args.t]
              Multiplier=10**digitDic[args.fo]
              Tolerance=tolDic[args.fi]
              FirstThreeDigits=str(FirstDigit)+str(SecondDigit)+str(ThirdDigit)

              Resis=int(FirstThreeDigits)*Multiplier
              Resis=Resis/1000
              print(Resis,"Kilo OHMS",Tolerance)
              
              



