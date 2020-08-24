var randomnumber= 0;
var string ="";
var str1 ="";
var answer=0;

function startGame()
{   document.getElementById('tips').innerHTML="* Guess a number between 0 and 100";
    randomnumber=Math.round(Math.random()*100);
    document.getElementById('difficulity').style.visibility='hidden';
    document.getElementById('input').style.visibility='visible';
    document.getElementById('myMsg').style.visibility='visible';
    document.timerform.START.disabled=true;


    if(document.timerform.time[0].checked)
    var time=60;

    if(document.timerform.time[1].checked)
    var time=30;

    if(document.timerform.time[2].checked)
    var time=20;

    document.getElementById('emailmsg').innerHTML=time;

    x=setInterval("startCountDown()",1000);

}


function startCountDown()
{
  number=parseInt(document.getElementById('emailmsg').innerHTML);
  --number;
  document.getElementById('emailmsg').innerHTML=number;
  if (number==-1)
  {
    clearInterval(x);
    document.timerform.START.disabled=false;
    document.getElementById('difficulity').style.visibility='visible';
    document.getElementById('input').style.visibility='hidden'
    document.getElementById('emailmsg').innerHTML=0;

    var string2 = document.getElementById('tips').innerHTML;
    var str2=string2 + "<br /> <font size='6' color='Green'>* Time is Over, The Secret Number Was " +randomnumber + "</font>";
    document.getElementById('tips').innerHTML = str2;

    alert("Time is Over, The Secret Number Was " +randomnumber);

    setTimeout(redirect, 2000);

  }

}

function checkanswers()
{
  answer=document.getElementById("guess").value;
  var exp=/^([0-9]|[1-9][0-9]|100)$/;

  if(!exp.test(answer))
  {
      string = document.getElementById('tips').innerHTML;
      var str1=string + "<br /> <font color='purple'>* Invalid Entered Value = "+answer+"</font>";
      document.getElementById('tips').innerHTML = str1;
  }


  else if(parseInt(answer)<randomnumber)
  {
      string = document.getElementById('tips').innerHTML;
      str1=string + "<br /> <font color='yellow'>* You Guessed "+answer+",Try Bigger Number</font>";
      document.getElementById('tips').innerHTML = str1;
  }

  else if(parseInt(answer)>randomnumber)
  {
      string = document.getElementById('tips').innerHTML;
      str1=string + "<br /> <font color='red'> </center> * You Guessed "+answer+",Try Smaller Number </center> </font>";
      document.getElementById('tips').innerHTML = str1;
  }

  else if(randomnumber==(parseInt(answer)))
  {
      string = document.getElementById('tips').innerHTML;
      str1=string + "<br /> <font size='6' color='Green'>* Hooray,You Won, "+answer+" Is The Correct Number</font>";
      document.getElementById('tips').innerHTML = str1;
      clearInterval(x);
      document.timerform.START.disabled=false;
      document.getElementById('difficulity').style.visibility='visible';
      document.getElementById('input').style.visibility='hidden';

      alert("Hooray,You Won, "+answer+" Is The Correct Number");
      setTimeout(redirect, 2000);
  }

}

function redirect(){
     window.location.href = "/guessgame/NULL";
  }
