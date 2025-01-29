from sympy import *


def no_eq_given(rcoef,pcoef,rinit,pinit):
    K = float(input("Type the equilibrium constant for the equation: "))
    Q = 1
    x = symbols("x")
    er = []
    ep = []
    try:
        for i in range(len(pcoef)):
            Q *= pinit[i] ** pcoef[i]
        for i in range(len(rcoef)):
            Q /= rinit[i] ** rcoef[i]
        if Q > K:
            for i in range(len(rcoef)):
                er.append(rinit[i] + rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] - pcoef[i] * x)
        elif Q < K:
            for i in range(len(rcoef)):
                er.append(rinit[i] - rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] + pcoef[i] * x)
        elif Q!= 0:
            print("Reaction is at equilibrium")
            for i in range(len(rcoef)):
                er.append(rinit[i])
            for i in range(len(pcoef)):
                ep.append(pinit[i])
        elif 0. in pinit:
            for i in range(len(rcoef)):
                er.append(rinit[i] - rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] + pcoef[i] * x)
    except:
        if 0. in rinit:
            for i in range(len(rcoef)):
                er.append(rinit[i] + rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] - pcoef[i] * x)
        if 0. in pinit:
            for i in range(len(rcoef)):
                er.append(rinit[i] - rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] + pcoef[i] * x)
    print(ep)
    print(er)
    equation = 1.0
    buffer = 1.0
    for i in range(len(ep)):
        equation *= ep[i] ** pcoef[i]
    for i in range(len(er)):
        buffer *= er[i] ** rcoef[i]
    equation -= buffer * K
    print(equation)
    equil = solve(equation,x)
    print(equil)
    conchange = 0
    for i in equil:
        try:
            flag = False
            if i < 0:
                continue
            for j in range(len(ep)):
                if ep[j].subs(x,i) < 0:
                    flag = True
            for j in range(len(er)):
                if er[j].subs(x,i) < 0:
                    flag = True
            if flag:
                continue
            else:
                conchange = i
        except:
            continue
    print("x =",conchange)
    for i in range(len(er)):
        print("Equilibrium concentration of reactant #{} = {}".format(i+1,er[i].subs(x,conchange)))
    for i in range(len(ep)):
        print("Equilibrium concentration of product #{} = {}".format(i + 1, ep[i].subs(x, conchange)))


def fivepercent(rcoef,pcoef,rinit,pinit):
    K = float(input("Type the equilibrium constant for the equation: "))
    x = symbols("x")
    er = []
    er5 = []
    ep = []
    ep5 = []
    if K > 1:
        for i in range(len(rcoef)):
            er5.append(rinit[i] + rcoef[i] * x)
            er.append(rinit[i] + rcoef[i] * x)
        for i in range(len(pcoef)):
            ep5.append(pinit[i])
            ep.append(pinit[i]-pcoef[i]*x)
    if K < 1:
        for i in range(len(rcoef)):
            er5.append(rinit[i])
            er.append(rinit[i]-rcoef[i]*x)
        for i in range(len(pcoef)):
            ep5.append(pinit[i] + pcoef[i] * x)
            ep.append(pinit[i] + pcoef[i] * x)
    print(ep5)
    print(er5)
    equation = 1.0
    buffer = 1.0
    for i in range(len(ep)):
        equation *= ep5[i] ** pcoef[i]
    for i in range(len(er)):
        buffer *= er5[i] ** rcoef[i]
    equation -= buffer * K
    print(equation)
    equil = solve(equation, x)
    print(equil)
    conchange = 0
    for i in equil:
        try:
            flag = False
            if i < 0:
                continue
            for j in range(len(ep)):
                if ep[j].subs(x, i) < 0:
                    flag = True
            for j in range(len(er)):
                if er[j].subs(x, i) < 0:
                    flag = True
            if flag:
                continue
            else:
                conchange = i
        except:
            continue
    print("x =", conchange)
    for i in range(len(er)):
        print("Equilibrium concentration of reactant #{} = {}".format(i + 1, er[i].subs(x, conchange)))
    for i in range(len(ep)):
        print("Equilibrium concentration of product #{} = {}".format(i + 1, ep[i].subs(x, conchange)))


def eq_given(rcoef,pcoef,rinit,pinit,type):
    pos = int(input("Which reactant/product is it? (type 1 for 1st reactant/product, 2 for second reactant/product etc.) "))
    pos -= 1
    eqi = float(input("Type the equilibrium concentration for that species"))
    x = symbols("x")
    er = []
    ep = []
    if type == "r":
        if eqi - rinit[pos] > 0:
            for i in range(len(rcoef)):
                er.append(rinit[i] + rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] - pcoef[i] * x)
        else:
            for i in range(len(rcoef)):
                er.append(rinit[i] - rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] + pcoef[i] * x)
    elif type == "p":
        if eqi - pinit[pos] > 0:
            for i in range(len(rcoef)):
                er.append(rinit[i] - rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] + pcoef[i] * x)
        else:
            for i in range(len(rcoef)):
                er.append(rinit[i] + rcoef[i] * x)
            for i in range(len(pcoef)):
                ep.append(pinit[i] - pcoef[i] * x)
    print(ep)
    print(er)
    if type == "r":
        conchange = solve((er[pos]-eqi),x)[0]
    elif type =="p":
        conchange = solve((ep[pos] - eqi), x)[0]
    print("x =", conchange)
    for i in range(len(er)):
        print("Equilibrium concentration of reactant #{} = {}".format(i + 1, er[i].subs(x, conchange)))
    for i in range(len(ep)):
        print("Equilibrium concentration of product #{} = {}".format(i + 1, ep[i].subs(x, conchange)))
    K = 1
    for i in range(len(er)):
        K/= er[i].subs(x,conchange)
    for i in range(len(ep)):
        K*= ep[i].subs(x,conchange)
    print("The equilibrium constant is",K)


coeffreact = input("Type coefficients of relevant reactants (commas): ")
coeffreact_list = coeffreact.split(",")
coeffprod = input("Type coefficients of relevant products (commas): ")
coeffprod_list = coeffprod.split(",")
for i in range(len(coeffprod_list)):
    coeffprod_list[i] = float(coeffprod_list[i])
for i in range(len(coeffreact_list)):
    coeffreact_list[i] = float(coeffreact_list[i])
ir = []
ip = []
for i in range(len(coeffreact_list)):
    ir.append(float(input("Type the initial concentration of the reactant #{}: ".format(i+1))))
for i in range(len(coeffprod_list)):
    ip.append(float(input("Type the initial concentration of the product #{}: ".format(i+1))))
prob = input("Is an equilibrium concentration value given? (type yes or no): ")
if prob.lower() == "yes":
    r_or_p = (input("Is the equilibrium concentration given for a product or a reactant? (type p or r respectively) "))
    eq_given(coeffreact_list,coeffprod_list,ir,ip,r_or_p.lower())

if prob.lower() != "yes":
    prob = (input("Can the five percent rule be applied? (type yes or no): "))
    if prob.lower() != "yes":
        no_eq_given(coeffreact_list, coeffprod_list, ir, ip)
    else:
        fivepercent(coeffreact_list, coeffprod_list, ir, ip)
