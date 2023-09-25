print("Ciao io sono Quizzi!\nTu come ti chiami?\n")
name = input()
print("Ciao " + name + "! Vuoi ripassare con me il NetWorking?^^")
risp=input()
consenso= "si"
if risp == consenso:
    print("Perfetto! Allora cominciamo!\nBuona Fortuna!")
else :
    print("Ma che scansafatiche!la tua risposta non mi piace!\nSti cazzi ora lo fai lo stesso!")
print("Bene, cominciamo con la prima domanda!\nRispondi con le lettere maiuscole!\nAh,se ne farai giuste più di 8 ti verrà assegnata la spilla onorevole di super studente!")
punteggio = 0

print("1- Quale funzionalità è fornita da DHCP?\nA:Test di connettività\nB:Assegnazione automatica di un indirizzo IP\nC:Gestione degli switch Remoti\nD:Traduzione indirizzi IP in nomi di dominio")
b=input()
risposta_giusta="B"
if b == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la B")

  
print("2-Quali indirizzi vengono mappati da ARP?\nA:Indirizzo IPV4 di destinazione all'indirizzo MAC di destinazione\nB:Indirizzo MAC di destinazione all'indirizzo IPV4 di origine\nC:Indirizzo ipv4 di destinazione al nome host di destinazione\nD:Indirizzo IPV4 di destinazione all'indirizzo MAC di origine")
a=input()
risposta_giusta="A"
if a == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la A")


print("3-Quale funzionalità del layer di trasporto viene utilizzata per garantire l'istituzione della sessione?\nA:Numero di sequenza del protocollo UDP\nB:UDP ACK flag\nC:Stretta di manoThree-Way TCP\nD:Numero di Porta TCP")
c=input()
risposta_giusta="C"
if c == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la C")


print("4-Quale tipo di progettazione di comunicazione inter-VLAN richiede la configurazione di più sottointerfacce?\nA:Router on a stick\nB:Routing per la VLAN di gestione\nC:Routing tramite uno switch multilayer\nD:Routing inter-VLAN legacy")
a=input()
risposta_giusta="A"
if a == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la A")


print("5-Quale valore determina il root bridge quando tutti gli switch collegati da collegamenti trunk hanno configurazioni STP predefinite?\nA:Bridge Priority\nB:ID VLAN\nC:Extended System ID\nD:Indirizzo MAC")
d=input()
risposta_giusta="D"
if d == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la D")

print("6-Quale comando fornirà informazioni sullo stato di tutte le interfacce incluso il numero di giant, runt e collisioni sull'interfaccia?\nA:show ip interface brief\nB:show running-config\nC:show history\nD:show interfaces")
d=input()
risposta_giusta="D"
if d == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la D")

print("7-Qual è l'ordine dei tipi di pacchetti utilizzati da un router OSPF per stabilire la convergenza?\nA:Hello, LSAck, LSU, LSR, DBD\nB:Hello, DBD, LSR, LSU, LSAck\nC:LSU, LSAck, Hello, DBD, LSR\nD:LSAck, Hello, DBD, LSU, LSR")
b=input()
risposta_giusta="B"
if b == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la B")


print("8-Quale'è il comando corretto per negare il traffico ftp alla rete 192.168.16.0/24 verso il server 192.168.50.101 e consentire tutto il resto ?\nA:permit ip any any\ndeny tcp 192.168.16.0 0.0.0.255 host 192.168.50.101 eq 21\n\nB:deny ip 192.168.16.0 0.0.0.255 host 192.168.50.101 eq 21\npermit ftp any any\n\nC:deny tcp 192.168.16.0 0.0.0.255 host 192.168.50.101 eq 21\npermit ip any any\n\nD:deny ftp 192.168.16.0 0.0.0.255 host 192.168.50.101 eq 21\npermit tcp any any")
c=input()
risposta_giusta="C"
if c == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la C")


print("9-Quale versione di NAT consente a molti host all'interno di una rete privata di utilizzare contemporaneamente un singolo inside global address per la connessione a Internet?\nA:PAT\nB:Nat Statico\nC:Nat Smart\nD:NAT Dinamico")
a=input()
risposta_giusta="A"
if a == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la A")


print("10-Qual è una funzione dei pacchetti hello OSPF?\nA:richiedere record specifici dello stato del collegamento dai router vicini\nB:Scoprire i vicini e costruire adiacenze tra di loro\nC:garantire la sincronizzazione del database tra router\nD:inviare record dello stato del collegamento specificamente richiesti")
b=input()
risposta_giusta="B"
if b == risposta_giusta:
    print("risposta corretta bro!")
    punteggio +=1
else :
    print("Mi dispiace, la risposta corretta era la B")

print("il tuo punteggio finale è di " + str(punteggio))

print("Mi è piaciuto ripassare con te, ti ringrazio per il tempo dedicatomi e ti auguro buon fine corso!")


    
