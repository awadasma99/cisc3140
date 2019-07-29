
(define (is-list lst)
  (if (null? lst)
      0 ;; return 0 if list is empty
      lst ;; else return lst
  ) ;; end if
) ;; end sum-list


;;; TEST Cases
(is-list '())        ; test empty list
(is-list '(1 2 3))   ; test list with values



(define (r2 x) 
  (let ( ( r (reverse x) ))
       (append r r)
  ))

(r2 '(1 2))




