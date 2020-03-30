import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class BuildlistService {

  private _url: string;

  constructor(
    private _httpClient: HttpClient
  ) {
    this._url = 'http://localhost:8000';
  }

  public getInfo = () => this._httpClient.get(this._url)
    .pipe(map((data: any) => data))

}
