import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-divider',
  templateUrl: './divider.component.html',
  styleUrls: ['./divider.component.css']
})
export class DividerComponent implements OnInit {

  @Input() content: string;
  @Input() background: string;

  constructor() { }

  ngOnInit() {
    // document.getElementById('hr') as HTML = this.content;
  }

}
