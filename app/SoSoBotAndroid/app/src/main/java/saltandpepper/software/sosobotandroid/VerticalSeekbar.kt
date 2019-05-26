package saltandpepper.software.sosobotandroid

import android.content.Context
import android.graphics.Canvas
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.widget.SeekBar

/**
 * Solution based on https://stackoverflow.com/questions/3333658/how-to-make-a-vertical-seekbar-in-android
 */
class VerticalSeekBar(context: Context, attrs: AttributeSet) : SeekBar(context, attrs) {

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(h, w, oldh, oldw)
    }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        super.onMeasure(heightMeasureSpec, widthMeasureSpec)
        setMeasuredDimension(measuredHeight, measuredWidth)
    }

    override fun onDraw(c: Canvas) {
        c.rotate(-90f)
        c.translate(-height.toFloat(),0f)

        super.onDraw(c)
    }

    override fun onTouchEvent(event: MotionEvent) : Boolean {
        if (!isEnabled) {
            return false
        }

        when (event.action) {
            MotionEvent.ACTION_DOWN,
            MotionEvent.ACTION_MOVE,
            MotionEvent.ACTION_UP -> {
                progress = max - (max * event.y / height).toInt()
                Log.i("Progress", progress.toString())
                onSizeChanged(width, height, 0, 0)
            }
        }
        return true
    }

}