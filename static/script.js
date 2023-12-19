let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo-header');
let logoSpan = document.querySelectorAll('.logo'); // Update this line

console.log("hello");

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                console.log("Adding 'active' class");
                span.classList.add('active');
            }, (idx + 1) * 400);
        });
        setTimeout(() => {
            logoSpan.forEach((span, idx) => {
                setTimeout(() => {
                    console.log("Adding 'fade' class");
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 400);
            });
        }, 2000);
    });
    setTimeout(() => {
        intro.style.top = '-100vh';
    },2300);
    });
    /*window.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            logoSpan.forEach((span, idx) => {
                setTimeout(() => {
                    span.classList.add('active');
                }, (idx + 1) * 400);
            });
            setTimeout(() => {
                logoSpan.forEach((span, idx) => {
                    setTimeout(() => {
                        span.classList.remove('active');
                        span.classList.add('fade');
                    }, (idx + 1) * 400);
                });
            }, 2000);
        });
        setTimeout(() => {
            intro.style.top = '-100vh';
        });
    });*/