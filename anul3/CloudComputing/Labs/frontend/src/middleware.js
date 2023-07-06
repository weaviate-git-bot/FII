import { NextResponse } from 'next/server'

export function middleware(request) {   
  const url = request.nextUrl.clone()   
  if (url.pathname === '/') {
    url.pathname = '/jobs'
    return NextResponse.redirect(url)   
  } 
}