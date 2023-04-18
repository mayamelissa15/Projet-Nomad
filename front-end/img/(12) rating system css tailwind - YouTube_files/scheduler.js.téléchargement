(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var f;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
function g(){var a=ba,b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];if(b)return b.call(a);if("number"==typeof a.length)return{next:aa(a)};throw Error(String(a)+" is not an iterable or ArrayLike");}
var ca="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},h;
if("function"==typeof Object.setPrototypeOf)h=Object.setPrototypeOf;else{var k;a:{var ha={a:!0},l={};try{l.__proto__=ha;k=l.a;break a}catch(a){}k=!1}h=k?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var m=h,n=this||self;
function p(a){a=a.split(".");for(var b=n,c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function q(a,b){a=a.split(".");var c=n;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
;var t,u=p("CLOSURE_FLAGS"),v=u&&u[610401301];t=null!=v?v:!1;var w,x=n.navigator;w=x?x.userAgentData||null:null;function y(a){return t?w?w.brands.some(function(b){return(b=b.brand)&&-1!=b.indexOf(a)}):!1:!1}
function z(a){var b;a:{if(b=n.navigator)if(b=b.userAgent)break a;b=""}return-1!=b.indexOf(a)}
;function A(){return t?!!w&&0<w.brands.length:!1}
function B(){return A()?y("Chromium"):(z("Chrome")||z("CriOS"))&&!(A()?0:z("Edge"))||z("Silk")}
;!z("Android")||B();B();z("Safari")&&(B()||(A()?0:z("Coast"))||(A()?0:z("Opera"))||(A()?0:z("Edge"))||(A()?y("Microsoft Edge"):z("Edg/"))||A()&&y("Opera"));function C(){this.s=this.s;this.B=this.B}
C.prototype.s=!1;C.prototype.dispose=function(){this.s||(this.s=!0,this.G())};
C.prototype.G=function(){if(this.B)for(;this.B.length;)this.B.shift()()};var D=n.window,E,F,G=(null==D?void 0:null==(E=D.yt)?void 0:E.config_)||(null==D?void 0:null==(F=D.ytcfg)?void 0:F.data_)||{};q("yt.config_",G);function H(a,b){return a in G?G[a]:b}
;function I(a,b){a=J(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function J(a){var b=H("EXPERIMENTS_FORCED_FLAGS",{})||{};return void 0!==b[a]?b[a]:H("EXPERIMENT_FLAGS",{})[a]}
;var ia=I("web_emulated_idle_callback_delay",300),K=1E3/60-3,ba=[8,5,4,3,2,1,0];
function L(a){a=void 0===a?{}:a;C.call(this);this.i=[];this.h={};this.D=this.g=0;this.C=this.l=!1;this.u=[];this.A=this.F=!1;for(var b=g(),c=b.next();!c.done;c=b.next())this.i[c.value]=[];this.j=0;this.N=a.timeout||1;this.o=K;this.m=0;this.H=this.R.bind(this);this.M=this.T.bind(this);this.J=this.O.bind(this);this.K=this.P.bind(this);this.L=this.S.bind(this);if(b=!!window.requestIdleCallback&&!!window.cancelIdleCallback)b=J("disable_scheduler_requestIdleCallback"),b=!("string"===typeof b&&"false"===
b?0:b);this.I=b;(this.v=!1!==a.useRaf&&!!window.requestAnimationFrame)&&document.addEventListener("visibilitychange",this.H)}
L.prototype=ca(C.prototype);L.prototype.constructor=L;if(m)m(L,C);else for(var M in C)if("prototype"!=M)if(Object.defineProperties){var N=Object.getOwnPropertyDescriptor(C,M);N&&Object.defineProperty(L,M,N)}else L[M]=C[M];function O(a,b){var c=Date.now();P(b);b=Date.now()-c;a.l||(a.o-=b)}
function Q(a,b,c,d){++a.D;if(10===c)return O(a,b),a.D;var e=a.D;a.h[e]=b;a.l&&!d?a.u.push({id:e,priority:c}):(a.i[c].push(e),a.C||a.l||(0!==a.g&&R(a)!==a.m&&S(a),a.start()));return e}
function T(a){a.u.length=0;for(var b=5;0<=b;b--)a.i[b].length=0;a.i[8].length=0;a.h={};S(a)}
function R(a){if(a.i[8].length){if(a.A)return 4;if(!document.hidden&&a.v)return 3}for(var b=5;b>=a.j;b--)if(0<a.i[b].length)return 0<b?!document.hidden&&a.v?3:2:1;return 0}
function U(a){var b=p("yt.logging.errors.log");b&&b(a)}
function P(a){try{a()}catch(b){U(b)}}
function ja(a){for(var b=g(),c=b.next();!c.done;c=b.next())if(a.i[c.value].length)return!0;return!1}
f=L.prototype;f.P=function(a){var b=void 0;a&&(b=a.timeRemaining());this.F=!0;V(this,b);this.F=!1};
f.T=function(){V(this)};
f.O=function(){ka(this)};
f.S=function(a){this.A=!0;var b=R(this);4===b&&b!==this.m&&(S(this),this.start());V(this,void 0,a);this.A=!1};
f.R=function(){document.hidden||ka(this);this.g&&(S(this),this.start())};
function ka(a){S(a);a.l=!0;for(var b=Date.now(),c=a.i[8];c.length;){var d=c.shift(),e=a.h[d];delete a.h[d];e&&P(e)}la(a);a.l=!1;ja(a)&&a.start();a.o-=Date.now()-b}
function la(a){for(var b=0,c=a.u.length;b<c;b++){var d=a.u[b];a.i[d.priority].push(d.id)}a.u.length=0}
function V(a,b,c){a.A&&4===a.m&&a.g||S(a);a.l=!0;b=Date.now()+(b||a.o);for(var d=a.i[5];d.length;){var e=d.shift(),r=a.h[e];delete a.h[e];if(r)try{r(c)}catch(sa){U(sa)}}for(d=a.i[4];d.length;)c=d.shift(),e=a.h[c],delete a.h[c],e&&P(e);d=a.F?0:1;d=a.j>d?a.j:d;if(!(Date.now()>=b)){do{a:{c=a;e=d;for(r=3;r>=e;r--)for(var da=c.i[r];da.length;){var ea=da.shift(),fa=c.h[ea];delete c.h[ea];if(fa){c=fa;break a}}c=null}c&&P(c)}while(c&&Date.now()<b)}a.l=!1;la(a);a.o=K;ja(a)&&a.start()}
f.start=function(){this.C=!1;if(0===this.g)switch(this.m=R(this),this.m){case 1:var a=this.K;this.g=this.I?window.requestIdleCallback(a,{timeout:3E3}):window.setTimeout(a,ia);break;case 2:this.g=window.setTimeout(this.M,this.N);break;case 3:this.g=window.requestAnimationFrame(this.L);break;case 4:this.g=window.setTimeout(this.J,0)}};
function S(a){if(a.g){switch(a.m){case 1:var b=a.g;a.I?window.cancelIdleCallback(b):window.clearTimeout(b);break;case 2:case 4:window.clearTimeout(a.g);break;case 3:window.cancelAnimationFrame(a.g)}a.g=0}}
f.G=function(){T(this);S(this);this.v&&document.removeEventListener("visibilitychange",this.H);C.prototype.G.call(this)};var W=p("yt.scheduler.instance.timerIdMap_")||{},ma=I("kevlar_tuner_scheduler_soft_state_timer_ms",800),X=0,Y=0;function Z(){var a=p("ytglobal.schedulerInstanceInstance_");if(!a||a.s)a=new L(H("scheduler")||{}),q("ytglobal.schedulerInstanceInstance_",a);return a}
function na(){oa();var a=p("ytglobal.schedulerInstanceInstance_");a&&(a&&"function"==typeof a.dispose&&a.dispose(),q("ytglobal.schedulerInstanceInstance_",null))}
function oa(){T(Z());for(var a in W)W.hasOwnProperty(a)&&delete W[Number(a)]}
function pa(a,b,c){if(!c)return c=void 0===c,-Q(Z(),a,b,c);var d=window.setTimeout(function(){var e=Q(Z(),a,b);W[d]=e},c);
return d}
function qa(a){var b=Z();O(b,a)}
function ra(a){var b=Z();if(0>a)delete b.h[-a];else{var c=W[a];c?(delete b.h[c],delete W[a]):window.clearTimeout(a)}}
function ta(a){var b=p("ytcsi.tick");b&&b(a)}
function ua(){ta("jse");va()}
function va(){window.clearTimeout(X);Z().start()}
function wa(){var a=Z();S(a);a.C=!0;window.clearTimeout(X);X=window.setTimeout(ua,ma)}
function xa(){window.clearTimeout(Y);Y=window.setTimeout(function(){ta("jset");ya(0)},ma)}
function ya(a){xa();var b=Z();b.j=a;b.start()}
function za(a){xa();var b=Z();b.j>a&&(b.j=a,b.start())}
function Aa(){window.clearTimeout(Y);var a=Z();a.j=0;a.start()}
;p("yt.scheduler.initialized")||(q("yt.scheduler.instance.dispose",na),q("yt.scheduler.instance.addJob",pa),q("yt.scheduler.instance.addImmediateJob",qa),q("yt.scheduler.instance.cancelJob",ra),q("yt.scheduler.instance.cancelAllJobs",oa),q("yt.scheduler.instance.start",va),q("yt.scheduler.instance.pause",wa),q("yt.scheduler.instance.setPriorityThreshold",ya),q("yt.scheduler.instance.enablePriorityThreshold",za),q("yt.scheduler.instance.clearPriorityThreshold",Aa),q("yt.scheduler.initialized",!0));}).call(this);
