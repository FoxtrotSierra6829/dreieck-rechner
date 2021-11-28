# Copyright (c), 2021, Florian Scheuner 
print("***Nicht für schriftliche")
print("Leistungsnachweise zulässig***")
i=1
while i==1:
        print("---------------")
        print("Dreieck-Rechner")
        print("---------------")
        import math as m
#ask for given variables
        try:
        	a = float(input("a="))
        except:
                	a=0
        try:
        	b = float(input("b="))
        except:
        	b=0
        try:
        	c=float(input("c="))
        except:
        	c=0
        try:
        	alpha=float(input("α="))
        except:
        	alpha=0
        try:
        	beta=float(input("β="))
        except:
        	beta=0
        try:
        	gamma=float(input("γ="))
        except:
        	gamma=0

#transform into radians
        alpha = m.radians(alpha)
        beta = m.radians(beta)
        gamma = m.radians(gamma)

#look up what we know
        query=""
        if a>0:
        	query = query+"a"
        if b>0:
        	query = query+"b"
        if c>0:
        	query = query+"c"
        if alpha>0:
        	query=query+"alpha"
        if beta>0:
        	query=query+"beta"
        if gamma>0:
        	query=query+"gamma"
#look up the answer
        print("---------------")
        if query=="abcalphabetagamma":
        	A=0.5*a*b*m.sin(gamma)
        	print("A=", A)

#1 lenght not given 	
        elif query=="bcalphabetagamma":
        	a=m.sqrt(b**2+c**2-2*b*c*m.cos(alpha))
        	A=0.5*a*b*m.sin(gamma)
        	print("a=", a)
        	print("A=", A)
        elif query=="acalphabetagamma":
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
                A=0.5*a*b*m.sin(gamma)
                print("b=", b)
                print("A=", A)
        elif query=="abalphabetagamma":
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("c=", c)
                print("A=", A)
                
#2 lenghts not given
        elif query=="calphabetagamma":
               a=m.sin(alpha)*c/m.sin(gamma)
               b=m.sin(beta)*c/m.sin(gamma)
               A=0.5*a*b*m.sin(gamma)
               print("a=", a)
               print("b=", b)
               print("A=", A)
        elif query=="balphabetagamma":
                a=m.sin(alpha)*b/m.sin(beta)
                c=m.sin(gamma)*b/m.sin(beta)
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("c=", c)
                print("A=", A)
        elif query=="aalphabetagamma":
                b=m.sin(beta)*a/m.sin(alpha)
                c=m.sin(gamma)*a/m.sin(alpha)
                A=0.5*a*b*m.sin(gamma)
                print("b=", b)
                print("c=", c)
                print("A=", A)
                
#1 angle not given
        elif query=="abcbetagamma":
                alpha=180-m.degrees(beta)-m.degrees(gamma)
                A=0.5*a*b*m.sin(gamma)
                print("α=", alpha)
                print("A=", A)
        elif query=="abcalphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                A=0.5*a*b*m.sin(gamma)
                print("β=", beta)
                print("A=", A)
        elif query=="abcalphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("γ=", gamma)
                print("A=", A)
                
#2 angles not given
        elif query=="abcgamma":
                if c>=a:
                        alpha=m.asin(a/c*m.sin(gamma))
                        if c>=b:
                                beta=m.asin(b/c*m.sin(gamma))
                                A=0.5*a*b*m.sin(gamma)
                                alpha=m.degrees(alpha)
                                beta=m.degrees(beta)
                                print("α=", alpha)
                                print("β=", beta)
                                print("A=", A)
                        else:
                                beta=180-m.degrees(alpha)-m.degrees(gamma)
                                A=0.5*a*b*m.sin(gamma)
                                alpha=m.degrees(alpha)
                                beta=m.degrees(beta)
                                print("α=", alpha)
                                print("β=", beta)
                                print("A=", A)
                else:
                        if c>=b:
                                beta=m.asin(b/c*m.sin(gamma))
                                alpha=180-m.degrees(beta)-m.degrees(gamma)
                                A=0.5*a*b*m.sin(gamma)
                                alpha=m.degrees(alpha)
                                beta=m.degrees(beta)
                                print("α=", alpha)
                                print("β=", beta)
                                print("A=", A)
                        else:
                                print("Fehler in der Berechnung.")
                                
        elif query=="abcbeta":
                if b>=a:
                        alpha=m.asin(a/b*m.sin(beta))
                        if b>=c:
                                gamma=m.asin(c/b*m.sin(beta))
                                A=0.5*a*b*m.sin(gamma)
                                alpha=m.degrees(alpha)
                                gamma=m.degrees(gamma)
                                print("α=", alpha)
                                print("γ=", gamma)
                                print("A=", A)
                        else:
                                gamma=180-m.degrees(alpha)-m.degrees(beta)
                                A=0.5*a*b*m.sin(m.radians(gamma))
                                alpha=m.degrees(alpha)
                                print("α=", alpha)
                                print("γ=", gamma)
                                print("A=", A)
                else:
                        if b>=c:
                                gamma=m.asin(c/b*m.sin(beta))
                                alpha=180-m.degrees(beta)-m.degrees(gamma)
                                A=0.5*a*b*m.sin(gamma)
                                alpha=m.degrees(alpha)
                                gamma=m.degrees(gamma)
                                print("α=", alpha)
                                print("γ=", gamma)
                                print("A=", A)
                        else:
                                print("Es sind 2 Dreiecke möglich.")
                                print("Feature wird nicht unterstüzt.")

        elif query=="abcalpha":
                if a>=b:
                        beta=m.asin(b/a*m.sin(alpha))
                        if a>=c:
                                gamma=m.asin(c/a*m.sin(alpha))
                                A=0.5*a*b*m.sin(gamma)
                                beta=m.degrees(beta)
                                gamma=m.degrees(gamma)
                                print("β=", beta)
                                print("γ=", gamma)
                                print("A=", A)
                        else:
                                gamma=180-m.degrees(alpha)-m.degrees(beta)
                                A=0.5*a*b*m.sin(m.radians(gamma))
                                beta=m.degrees(beta)
                                print("β=", beta)
                                print("γ=", gamma)
                                print("A=", A)
                else:
                        if a>=c:
                                gamma=m.asin(c/a*m.sin(alpha))
                                beta=180-m.degrees(alpha)-m.degrees(gamma)
                                A=0.5*a*b*m.sin(gamma)
                                beta=m.degrees(beta)
                                gamma=m.degrees(gamma)
                                print("β=", beta)
                                print("γ=", gamma)
                                print("A=", A)
                        else:
                                print("Es sind 2 Dreiecke möglich.")
                                print("Feature wird nicht unterstüzt.")
                
#1 lenght and 1 angle not given
        #a not given
        elif query=="bcbetagamma":
                alpha=180-m.degrees(beta)-m.degrees(gamma)
                a=m.sqrt(b**2+c**2-2*b*c*m.cos(m.radians(alpha)))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("α=", alpha)
                print("A=", A)
        elif query=="bcalphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                a=m.sqrt(b**2+c**2-2*b*c*m.cos(alpha))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("β=", beta)
                print("A=", A)
        elif query=="bcalphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(gamma)
                a=m.sqrt(b**2+c**2-2*b*c*m.cos(alpha))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("a=", a)
                print("γ=", gamma)
                print("A=", A)

        #b not given		
        elif query=="acbetagamma":
               alpha=180-m.degrees(beta)-m.degrees(gamma)
               b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
               A=0.5*a*b*m.sin(gamma)
               print("b=", b)
               print("α=", alpha)
               print("A=", A)
        elif query=="acalphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(m.radians(beta)))
                A=0.5*a*b*m.sin(gamma)
                print("b=", b)
                print("β=", beta)
                print("A=", A)
        elif query=="acalphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(gamma)
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("b=", b)
                print("γ=", gamma)
                print("A=", A)
			
        #c not given	
        elif query=="abbetagamma":
               alpha=180-m.degrees(beta)-m.degrees(gamma)
               c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
               A=0.5*a*b*m.sin(gamma)
               print("c=", c)
               print("α=", alpha)
               print("A=", A)
        elif query=="abalphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("c=", c)
                print("β=", beta)
                print("A=", A)
        elif query=="abalphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(m.radians(gamma)))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("c=", c)
                print("γ=", gamma)
                print("A=", A)
                
#2 lenghts and 1 angle not given
        elif query=="cbetagamma":
                alpha=180-m.degrees(beta)-m.degrees(gamma)
                a=m.sin(m.radians(alpha))*c/m.sin(gamma)
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("b=", b)
                print("α=", alpha)
                print("A=", A)
        elif query=="calphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                b=m.sin(m.radians(beta))*c/m.sin(gamma)
                a=m.sqrt(b**2+c**2-2*b*c*m.cos(alpha))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("b=", b)
                print("β=", beta)
                print("A=", A)
        elif query=="calphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                a=m.sin(alpha)*c/m.sin(m.radians(gamma))
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("a=", a)
                print("b=", b)
                print("γ=", gamma)
                print("A=", A)
        elif query=="bbetagamma":
                alpha=180-m.degrees(beta)-m.degrees(gamma)
                a=m.sin(m.radians(alpha))*b/m.sin(beta)
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("c=", c)
                print("α=", alpha)
                print("A=", A)
        elif query=="balphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                a=m.sin(alpha)*b/m.sin(m.radians(beta))
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("a=", a)
                print("c=", c)
                print("β=", beta)
                print("A=", A)
        elif query=="balphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                c=m.sin(m.radians(gamma))*b/m.sin(beta)
                a=m.sqrt(b**2+c**2-2*b*c*m.cos(alpha))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("a=", a)
                print("c=", c)
                print("γ=", gamma)
                print("A=", A)
        elif query=="abetagamma":
                alpha=180-m.degrees(beta)-m.degrees(gamma)
                b=m.sin(beta)*a/m.sin(m.radians(alpha))
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("b=", b)
                print("c=", c)
                print("α=", alpha)
                print("A=", A)
        elif query=="aalphagamma":
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                b=m.sin(m.radians(beta))*a/m.sin(alpha)
                c=m.sqrt(a**2+b**2-2*a*b*m.cos(gamma))
                A=0.5*a*b*m.sin(gamma)
                print("b=", b)
                print("c=", c)
                print("β=", beta)
                print("A=", A)
        elif query=="aalphabeta":
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                c=m.sin(m.radians(gamma))*a/m.sin(alpha)
                b=m.sqrt(a**2+c**2-2*a*c*m.cos(beta))
                A=0.5*a*b*m.sin(m.radians(gamma))
                print("b=", b)
                print("c=", c)
                print("γ=", gamma)
                print("A=", A)
                
#3 angles not given
        elif query=="abc":
        	alpha=m.degrees(m.acos((a**2-b**2-c**2)/(-2*b*c)))
        	beta=m.degrees(m.acos((b**2-a**2-c**2)/(-2*a*c)))
        	gamma=m.degrees(m.acos((c**2-a**2-b**2)/(-2*a*b)))
        	A=0.5*a*b*m.sin(m.radians(gamma))
        	print("α=", alpha)
        	print("β=", beta)
        	print("γ=", gamma)
        	print("A=", A)
        	

                
#1 lenghts and 2 angles not given
        elif query=="bcgamma":
                if c>=b:
                        beta=m.asin(b/c*m.sin(gamma))
                        alpha=180-m.degrees(beta)-m.degrees(gamma)
                        a=c/m.sin(gamma)*m.sin(m.radians(alpha))
                        beta=m.degrees(beta)
                        A=0.5*a*b*m.sin(gamma)
                        print("a=", a)
                        print("α=", alpha)
                        print("β=", beta)
                        print("A=", A)
                else:
                        beta=m.asin(b/c*m.sin(gamma))
                        alpha=180-m.degrees(beta)-m.degrees(gamma)
                        a=c/m.sin(gamma)*m.sin(m.radians(alpha))
                        beta=m.degrees(beta)
                        A=0.5*a*b*m.sin(gamma)
                        beta2=180-beta
                        alpha2=180-beta2-m.degrees(gamma)
                        a2=c/m.sin(gamma)*m.sin(m.radians(alpha2))
                        A2=0.5*a2*b*m.sin(gamma)
                        print("Dreieck 1")
                        print("a=", a)
                        print("α=", alpha)
                        print("β=", beta)
                        print("A=", A)
                        print("Dreieck 2")
                        print("a2=", a2)
                        print("α2=", alpha2)
                        print("β2=", beta2)
                        print("A2=", A2)
        elif query=="bcbeta":
                if b>=c:
                        gamma=m.asin(c/b*m.sin(beta))
                        alpha=180-m.degrees(beta)-m.degrees(gamma)
                        a=c/m.sin(gamma)*m.sin(m.radians(alpha))
                        A=0.5*a*b*m.sin(gamma)
                        gamma=m.degrees(gamma)
                        print("a=", a)
                        print("α=", alpha)
                        print("γ=", gamma)
                        print("A=", A)
                else:
                        gamma=m.asin(c/b*m.sin(beta))
                        alpha=180-m.degrees(beta)-m.degrees(gamma)
                        a=c/m.sin(gamma)*m.sin(m.radians(alpha))
                        A=0.5*a*b*m.sin(gamma)
                        gamma=m.degrees(gamma)
                        gamma2=180-gamma
                        alpha2=180-gamma2-m.degrees(beta)
                        a2=c/m.sin(gamma)*m.sin(m.radians(alpha2))
                        A2=0.5*a2*b*m.sin(m.radians(gamma2))
                        print("Dreieck 1")
                        print("a=", a)
                        print("α=", alpha)
                        print("γ=", gamma)
                        print("A=", A)
                        print("Dreieck 2")
                        print("a2=", a2)
                        print("α2=", alpha2)
                        print("γ2=", gamma2)
                        print("A2=", A2)
        elif query=="bcalpha":
                a=m.sqrt(b**2+c**2-(2*b*c*m.cos(alpha)))
                beta=m.asin(b/a*m.sin(alpha))
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                A=0.5*a*b*m.sin(m.radians(gamma))
                beta=m.degrees(beta)
                print("a=", a)
                print("β=", beta)
                print("γ=", gamma)
                print("A=", A)
        elif query=="acgamma":
                if c>=a:
                        alpha=m.asin(a/c*m.sin(gamma))
                        beta=180-m.degrees(alpha)-m.degrees(gamma)
                        b=c/m.sin(gamma)*m.sin(m.radians(beta))
                        alpha=m.degrees(alpha)
                        A=0.5*a*b*m.sin(gamma)
                        print("b=", b)
                        print("α=", alpha)
                        print("β=", beta)
                        print("A=", A)
                else:
                        alpha=m.asin(a/c*m.sin(gamma))
                        beta=180-m.degrees(alpha)-m.degrees(gamma)
                        b=c/m.sin(gamma)*m.sin(m.radians(beta))
                        alpha=m.degrees(alpha)
                        A=0.5*a*b*m.sin(gamma)
                        alpha2=180-alpha
                        beta2=180-alpha2-m.degrees(gamma)
                        b2=c/m.sin(gamma)*m.sin(m.radians(beta2))
                        A2=0.5*a*b2*m.sin(gamma)
                        print("Dreieck 1")
                        print("b=", b)
                        print("α=", alpha)
                        print("β=", beta)
                        print("A=", A)
                        print("Dreieck 2")
                        print("b2=", b2)
                        print("α2=", alpha2)
                        print("β2=", beta2)
                        print("A2=", A2)
        elif query=="acbeta":
                b=m.sqrt(a**2+c**2-(2*a*c*m.cos(beta)))
                alpha=m.asin(a/b*m.sin(beta))
                gamma=180-m.degrees(alpha)-m.degrees(beta)
                A=0.5*a*b*m.sin(m.radians(gamma))
                alpha=m.degrees(alpha)
                print("b=", b)
                print("α=", alpha)
                print("γ=", gamma)
                print("A=", A)
        elif query=="acalpha":
                if a>=c:
                        gamma=m.asin(c/a*m.sin(alpha))
                        beta=180-m.degrees(alpha)-m.degrees(gamma)
                        b=c/m.sin(gamma)*m.sin(m.radians(beta))
                        A=0.5*a*b*m.sin(gamma)
                        gamma=m.degrees(gamma)
                        print("b=", b)
                        print("β=", beta)
                        print("γ=", gamma)
                        print("A=", A)
                else:
                        gamma=m.asin(c/a*m.sin(alpha))
                        beta=180-m.degrees(alpha)-m.degrees(gamma)
                        b=c/m.sin(gamma)*m.sin(m.radians(beta))
                        A=0.5*a*b*m.sin(gamma)
                        gamma=m.degrees(gamma)
                        gamma2=180-gamma
                        beta2=180-gamma2-m.degrees(alpha)
                        b2=c/m.sin(gamma)*m.sin(m.radians(beta2))
                        A2=0.5*a*b2*m.sin(m.radians(gamma2))
                        print("Dreieck 1")
                        print("b=", b)
                        print("β=", beta)
                        print("γ=", gamma)
                        print("A=", A)
                        print("Dreieck 2")
                        print("b2=", b2)
                        print("β2=", beta2)
                        print("γ2=", gamma2)
                        print("A2=", A2)
        elif query=="abgamma":
                c=m.sqrt(a**2+b**2-(2*a*b*m.cos(gamma)))
                alpha=m.asin(a/c*m.sin(gamma))
                beta=180-m.degrees(alpha)-m.degrees(gamma)
                A=0.5*a*b*m.sin(gamma)
                alpha=m.degrees(alpha)
                print("c=", c)
                print("α=", alpha)
                print("β=", beta)
                print("A=", A)
        elif query=="abbeta":
                if b>=a:
                        alpha=m.asin(a/b*m.sin(beta))
                        gamma=180-m.degrees(alpha)-m.degrees(beta)
                        c=b/m.sin(beta)*m.sin(m.radians(gamma))
                        A=0.5*a*b*m.sin(m.radians(gamma))
                        alpha=m.degrees(alpha)
                        print("c=", c)
                        print("α=", alpha)
                        print("γ=", gamma)
                        print("A=", A)
                else:
                        alpha=m.asin(a/b*m.sin(beta))
                        gamma=180-m.degrees(alpha)-m.degrees(beta)
                        c=b/m.sin(beta)*m.sin(m.radians(gamma))
                        A=0.5*a*b*m.sin(m.radians(gamma))
                        alpha=m.degrees(alpha)
                        alpha2=180-alpha
                        gamma2=180-alpha2-m.degrees(beta)
                        c2=b/m.sin(beta)*m.sin(m.radians(gamma2))
                        A2=0.5*a*b*m.sin(m.radians(gamma2))
                        print("Dreieck 1")
                        print("c=", c)
                        print("α=", alpha)
                        print("γ=", gamma)
                        print("A=", A)
                        print("Dreieck 2")
                        print("c2=", c2)
                        print("α2=", alpha2)
                        print("γ2=", gamma2)
                        print("A2=", A2)
        elif query=="abalpha":
                if a>=b:
                        beta=m.asin(b/a*m.sin(alpha))
                        gamma=180-m.degrees(alpha)-m.degrees(beta)
                        c=b/m.sin(beta)*m.sin(m.radians(gamma))
                        A=0.5*a*b*m.sin(m.radians(gamma))
                        beta=m.degrees(beta)
                        print("c=", c)
                        print("β=", beta)
                        print("γ=", gamma)
                        print("A=", A)
                else:
                        beta=m.asin(b/a*m.sin(alpha))
                        gamma=180-m.degrees(alpha)-m.degrees(beta)
                        c=b/m.sin(beta)*m.sin(m.radians(gamma))
                        A=0.5*a*b*m.sin(m.radians(gamma))
                        beta=m.degrees(beta)
                        beta2=180-beta
                        gamma2=180-beta2-m.degrees(alpha)
                        c2=a/m.sin(alpha)*m.sin(m.radians(gamma2))
                        A2=0.5*a*b*m.sin(m.radians(gamma2))
                        print("Dreieck 1")
                        print("c=", c)
                        print("β=", beta)
                        print("γ=", gamma)
                        print("A=", A)
                        print("Dreieck 2")
                        print("c2=", c2)
                        print("β2=", beta2)
                        print("γ2=", gamma2)
                        print("A2=", A2)
        	
#2 lenghts and 2 angles not given
        elif query=="alphabetagamma":
        	print("Berechnung nicht möglich.")
        	print("Dreieck frei skalierbar.")
#3 lenghts and x angles not given
        else:
                print("Berechnung nicht möglich.")
                print("Es werden mindestens 3 Angaben benötigt.")

