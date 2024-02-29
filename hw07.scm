(define (square n) (* n n))

(define (pow base exp) 
  (cond ((= exp 0 )1)
        ((even? exp)(square(pow base(/ exp 2))))
        ((odd? exp) (* base(pow base(- exp 1))))))

(define (repeatedly-cube n x)  ;x^n so need to subtract 1 from n each time
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1)x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s))) 
; car - returns first elem in list 
; cdr - returns rest of list 

(define (cadr s)  ;return second elem of list 
  (car(cdr s)))  ;error earlier bc put (s) 

(define (caddr s) ;return third elem of list 
  (car(cdr(cdr s)))) 
