/*CORE*/var OdinT=(function(){var F=28.84,P=3.467,KS=1e9,KA=3.6e4,MW=69000;
function free(tt,shbg,alb){var T=tt*1e-9,S=shbg*1e-9,N=1+KA*alb/MW,a=N*KS,b=N+KS*(S-T),ft=(-b+Math.sqrt(b*b+4*a*T))/(2*a);
return{pmol:ft*1e12,pg:ft*1e12/P,pct:100*ft/T,bat:ft*N*1e9,batNg:ft*N*1e9*F,alb:(N-1)*ft*1e9,shbgB:tt-ft*N*1e9,N:N};}
return{F:F,P:P,free:free,toNg:function(n){return n*F;},toNmol:function(g){return g/F;},toPmol:function(g){return g*P;},toPg:function(p){return p/P;}};})();
if(typeof module!=='undefined'&&module.exports)module.exports=OdinT;/*/CORE*/
