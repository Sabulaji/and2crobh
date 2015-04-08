from gpiooutput import *
import RPi.GPIO as GPIO
from socket import *
import fcntl
import struct

akalin = '''
                                       /*
                                      +
                                     +
                                    +
                                    +
                                    [         >i>n[t
                                     */   #include<stdio.h>
                        /*2w0,1m2,]_<n+a m+o>r>i>=>(['0n1'0)1;
                     */int/**/main(int/**/n,char**m){FILE*p,*q;int        A,k,a,r,i/*
                   #uinndcelfu_dset<rsitcdti_oa.nhs>i/_*/;char*d="P%"   "d\n%d\40%d"/**/
                 "\n%d\n\00wb+",b[1024],y[]="yuriyurarararayuruyuri*daijiken**akkari~n**"
          "/y*u*k/riin<ty(uyr)g,aur,arr[a1r2a82*y2*/u*r{uyu}riOcyurhiyua**rrar+*arayra*="
       "yuruyurwiyuriyurara'rariayuruyuriyuriyu>rarararayuruy9uriyu3riyurar_aBrMaPrOaWy^?"
      "*]/f]`;hvroai<dp/f*i*s/<ii(f)a{tpguat<cahfaurh(+uf)a;f}vivn+tf/g*`*w/jmaa+i`ni("/**
     */"i+k[>+b+i>++b++>l[rb";int/**/u;for(i=0;i<101;i++)y[i*2]^="~hktrvg~dmG*eoa+%squ#l2"
     ":(wn\"1l))v?wM353{/Y;lgcGp`vedllwudvOK`cct~[|ju {stkjalor(stwvne\"gt\"yogYURUYURI"[
     i]^y[i*2+1]^4;/*!*/p=(n>1&&(m[1][0]-'-'||m[1][1]  !='\0'))?fopen(m[1],y+298):stdin;
      /*y/riynrt~(^w^)],]c+h+a+r+*+*[n>)+{>f+o<r<(-m]    =<2<5<64;}-]-(m+;yry[rm*])/[*
       */q=(n<3||!(m[2][0]-'-'||m[2][1]))?stdout /*]{     }[*/:fopen(m[2],d+14);if(!p||/*
       "]<<*-]>y++>u>>+r >+u+++y>--u---r>++i+++"  <)<      ;[>-m-.>a-.-i.++n.>[(w)*/!q/**/)
    return+printf("Can "  "not\x20open\40%s\40"    ""       "for\40%sing\n",m[!p?1:2],!p?/*
  o=82]5<<+(+3+1+&.(+  m  +-+1.)<)<|<|.6>4>-+(>    m-        &-1.9-2-)-|-|.28>-w-?-m.:>([28+
 */"read":"writ");for  (   a=k=u= 0;y[u];  u=2    +u){y[k++   ]=y[u];}if((a=fread(b,1,1024/*
,mY/R*Y"R*/,p/*U*/)/*          R*/ )>/*U{  */   2&& b/*Y*/[0]/*U*/=='P' &&4==/*"y*r/y)r\}
*/sscanf(b,d,&k,& A,&           i,  &r)&&        !   (k-6&&k -5)&&r==255){u=A;if(n>3){/*
]&<1<6<?<m.-+1>3> +:+ .1>3+++     .   -m-)      -;.u+=++.1<0< <; f<o<r<(.;<([m(=)/8*/
u++;i++;}fprintf   (q,    d,k,           u      >>1,i>>1,r);u  = k-5?8:4;k=3;}else
  /*]>*/{(u)=/*{   p> >u  >t>-]s                >++(.yryr*/+(    n+14>17)?8/4:8*5/
     4;}for(r=i=0  ;  ;){u*=6;u+=                (n>3?1:0);if    (y[u]&01)fputc(/*
      <g-e<t.c>h.a r  -(-).)8+<1.                 >;+i.(<)<     <)+{+i.f>([180*/1*
      (r),q);if(y[u   ]&16)k=A;if                               (y[u]&2)k--;if(i/*
      ("^w^NAMORI; {   I*/==a/*"                               )*/){/**/i=a=(u)*11
       &255;if(1&&0>=     (a=                                 fread(b,1,1024,p))&&
        ")]i>(w)-;} {                                         /i-f-(-m--M1-0.)<{"
         [ 8]==59/* */                                       )break;i=0;}r=b[i++]
            ;u+=(/**>>                                     *..</<<<)<[[;]**/+8&*
            (y+u))?(10-              r?4:2):(y[u]         &4)?(k?2:4):2;u=y[u/*
             49;7i\(w)/;}             y}ru\=*ri[        ,mc]o;n}trientuu ren (
             */]-(int)'`';}             fclose(          p);k= +fclose( q);
              /*] <*.na/m*o{ri{                       d;^w^;}  }^_^}}
               "   */   return  k-                -1+   /*\'   '-`*/
                     (   -/*}/   */0x01        );       {;{    }}
                            ;           /*^w^*/        ;}
'''
# print a

commands = {
    "c":gpiooutput().c,
    "l":gpiooutput().l,
    "w":gpiooutput().w,
    "s":gpiooutput().s,
    "a":gpiooutput().a,
    "d":gpiooutput().d
}

def run(command):
	# print command

	try:
		commands[command]()
	except Exception,e:
		print "Oops",e

def get_ip_address(ifname):
    s = socket(AF_INET, SOCK_DGRAM)
    return inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

###################################################################################################

#Main

print akalin

HOST = get_ip_address('wlan0')
print HOST

PORT = 8888
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

print ("listening on 8888")
print ("ctrl+c to quit")

try:
	while 1:
		c,addr = s.accept()
		print ("Connected by:",addr)
		while 1:
			command = c.recv(2).replace('\n','')
			print command
			if not command:
				break
			run(command)
		c.close()


except KeyboardInterrupt:
	pass

GPIO.cleanup()
s.close()
