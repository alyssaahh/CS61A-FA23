(define (ascending? s) 
    (cond ((null? s) #t)      ;empty list
          ((null? (cdr s)) #t)  ;list only 1 element 
          (else (and(<= (car s) (car(cdr s)))(ascending? (cdr s))))))  ;if first elem less than second then need to check second vs third --> recursion!

(define (my-filter pred s) ;recursion, return new list (cons)
    (cond ((null? s)nil) ;empty return empty list
          ((pred(car s)) (cons(car s) (my-filter pred (cdr s)))) ;apply pred to first elem if match then make include in new list then repeat for rest of elements
          (else (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) ;return a new list (cons)
    (cond ((null? lst1) lst2)
          ((null? lst2) lst1)
          (else (cons (car lst1)(cons (car lst2)(interleave(cdr lst1)(cdr lst2))))))) ;cons can only take 1 element so remember to separate 


;Hint: You may find it helpful to use filter with a lambda procedure to filter out repeats. To test if two numbers a and b are not equal, use (not (= a b)).
(define (no-repeats s) 
        (if (null? s)nil ; if empty return empty list
         (cons(car s);"else" make new list 
         (no-repeats(filter(lambda(x)(not (= (car s)x))) (cdr s)))))) ; [ARG 1: does first elem = x? if not return true] [ARG 2: rest of list]
        
        
        
    