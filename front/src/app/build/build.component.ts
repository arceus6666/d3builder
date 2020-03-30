import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BuildService } from './build.service';

@Component({
  selector: 'app-build',
  templateUrl: './build.component.html',
  styleUrls: ['./build.component.css']
})
export class BuildComponent implements OnInit {

  public _id: number;
  public _build: any;

  public position: Array<string>;

  constructor(
    private _route: ActivatedRoute,
    private _service: BuildService
  ) { }

  ngOnInit() {
    this._id = parseInt(this._route.snapshot.paramMap.get('id'), 10);
    this._service.getOne(this._id).subscribe((data: any) => {
      this._build = data;
      this.position = ['Home', 'Builds', data.name];
      // this.position.push(data.name);
      console.log(this.position);
    });
  }

}
