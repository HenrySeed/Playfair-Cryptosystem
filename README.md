# Playfair Python
Python implementation of a playfair cipher.

It can make a cipher grid based on a given key. Includes encryption and decryption functions. All you need to do is supply a key. 

For example to encrypt:
```python
encrypt('keyexample', 'messagetest')
```
outputs to
```python
'pk nr zc fy uk nz'
```

To decrypt:
```python
decrypt('keyexample', 'pk nr zc fy uk nz')
```
outputs to
```python
'messagetest'
```

Creating a new cipher and printing the class returns the grid if you want to encrypt/decrypt by hand.
```python
new_cipher = Playfair('playfairexample')
print(new_cipher)

p l a y f 
i r e x m 
b c d g h 
k n o q s 
t u v w z 

```
The cipher class is mostly used by the encrypt and decrypt functions. This is foremost a simple version of the Playfair cipher.
