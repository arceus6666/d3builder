import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class BuildService {

  private _url: string;

  constructor(
    private _httpClient: HttpClient
  ) {
    this._url = 'http://localhost:8000';
  }
  public getOne = (id: number) =>
    this._httpClient.get(`${this._url}/${id}`).pipe(map((data: any) => data))
}
