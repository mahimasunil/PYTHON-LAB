{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "37700e1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number:12\n",
      "Enter second number:18\n",
      "gcd(num1,num2): 6\n"
     ]
    }
   ],
   "source": [
    "def gcd(a,b): \n",
    "    if(b==0):\n",
    "        return a \n",
    "    else: return gcd(b,a%b)\n",
    "num1=int(input(\"Enter first number:\"))\n",
    "\n",
    "num2=int(input(\"Enter second number:\"))\n",
    "\n",
    "gc=gcd(num1,num2)\n",
    "print(\"gcd(num1,num2):\",gc) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "be1a31d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "def hello():\n",
    "    print(\"Hello world\")\n",
    "hello()\n",
    "    \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f95e3621",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter no 1:12\n",
      "Enter no 2:4\n",
      "sum 16\n"
     ]
    }
   ],
   "source": [
    "def sum():\n",
    "    print(\"sum\",a+b)\n",
    "a=int(input(\"Enter no 1:\"))\n",
    "b=int(input(\"Enter no 2:\"))\n",
    "sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e4869fd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter n5\n",
      "Enter an integer:12\n",
      "Enter an integer:35\n",
      "Enter an integer:50\n",
      "Enter an integer:79\n",
      "Enter an integer:21\n",
      "[12, 35, 50, 79, 21]\n",
      "After removing even numbers\n",
      "[35, 79, 21]\n"
     ]
    }
   ],
   "source": [
    "list=[]\n",
    "n=int(input(\"Enter n\"))\n",
    "for i in range(n):\n",
    "    num=int(input(\"Enter an integer:\"))\n",
    "    list.append(num);\n",
    "print(list)\n",
    "for i in list:\n",
    "    if i%2==0:\n",
    "        list.remove(i)\n",
    "print(\"After removing even numbers\")\n",
    "print(list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ab7a36d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
